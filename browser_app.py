import matplotlib.pyplot as plt
import pandas_datareader as pdr
from datetime import datetime
import streamlit as st
import pandas as pd
st.set_option('deprecation.showPyplotGlobalUse', False)


st.title('Comparing risk and return using the Moving Average Strategy')
st.markdown('[Investopedia on Moving Average](https://www.investopedia.com/articles/active-trading/052014/how-use-moving-average-buy-stocks.asp)')

ticker = st.sidebar.text_input('Enter a valid stock ticker', value = '^GSPC')
period = st.sidebar.number_input('Choose the moving average period (Days)',min_value = 2, max_value = 500, value=200)
start_balance = st.sidebar.number_input('Enter how much money you would like to start with', min_value = 1, value= 10000)

start_date = st.sidebar.text_input('Enter A Starting Date. Format YYYY/MM/DD:')
start_date = datetime.strptime(start_date,'%Y/%m/%d').date()

end_date = st.sidebar.text_input('Enter An Ending Date. Format YYYY/MM/DD:')
end_date = datetime.strptime(end_date,'%Y/%m/%d').date()
years = (end_date - start_date).days/ 365.25



def calculating_metrics(stock, years):
    # metrics for the base
    base_return_metric = round((stock['Baseline'][-1] / stock['Baseline'][0] - 1) * 100,2)
    base_cagr_metric = round((((stock['Baseline'][-1] / stock['Baseline'][0]) ** (1/years)) - 1) * 100, 2)
    base_dd_metric = round(((stock['Base_DD'] / stock['Base_Peak']).min() * 100), 2)
    
    # metrics for the Moving Average Strat
    ma_return_metric = round((stock['SMA_Strat'][-1] / stock['SMA_Strat'][0] - 1) * 100,2)
    ma_cagr_metric = round((((stock['SMA_Strat'][-1] / stock['SMA_Strat'][0]) ** (1/years)) - 1) * 100, 2)
    ma_dd_metric = round(((stock['MA_DD'] / stock['MA_Peak']).min() * 100), 2)
    
    return base_return_metric, base_cagr_metric, base_dd_metric, ma_return_metric, ma_cagr_metric, ma_dd_metric

def sma_eval():
    
    # getting the df based on user stock ticker
    stock = pdr.get_data_yahoo(ticker, start_date, end_date)
    
    # dropping extra columns
    stock.drop(['High', 'Low', 'Volume', 'Adj Close'], axis = 1, inplace = True)
    
    # getting the daily return 
    stock['Return'] = stock['Close'] / stock['Close'].shift(1)
    
    # dropping the first row now because it has a NaN
    stock.dropna(inplace=True)
    
    # getting the baseline (if you didn't buy or sell at all after initial purchase)
    stock['Baseline'] = stock['Return'].cumprod() * start_balance
    
    # adding in the columns for baseline peak & drawdown
    stock['Base_Peak'] = stock['Baseline'].cummax()
    stock['Base_DD'] = stock['Baseline'] - stock['Base_Peak']
    
    # getting the Simple Moving Average
    stock['SMA'] = stock['Close'].rolling(window=period).mean()
    
    # making a column to let us know when to buy and when to sell
    stock['Buy'] = (stock['Close'] > stock['SMA']) * 1
    
    # Keep in mind we will only start buying after we get the first SMA so not until the period time we got before
    stock['Updated_Return'] = np.where(stock['Buy'].shift(1) == 1, stock['Return'], 1.0)
    stock.dropna(inplace = True) 
    
    # column to keep track of the moving average strategy
    stock['SMA_Strat'] = stock['Updated_Return'].cumprod() * start_balance
    
    # columns for the SMA metrics
    stock['MA_Peak'] = stock['SMA_Strat'].cummax()
    stock['MA_DD'] = stock['SMA_Strat'] - stock['MA_Peak']
    
    # getting the metrics from the function above now that all the columns are made
    base_return_metric, base_cagr_metric, base_dd_metric, ma_return_metric, ma_cagr_metric, ma_dd_metric = calculating_metrics(stock, years)
    
    return stock

if st.sidebar.button('Run 🏃‍'):
	df = sma_eval()

	base_return_metric, base_cagr_metric, base_dd_metric, ma_return_metric, ma_cagr_metric, ma_dd_metric = calculating_metrics(df, years)

	plt.figure(figsize=(16, 8))
	plt.plot(df['Baseline'], label = 'Baseline')
	plt.plot(df['SMA_Strat'], label = 'Moving Averge Strategy')
	plt.xticks(fontsize = 12)
	plt.yticks(fontsize = 12)
	plt.legend(fontsize=14)
	st.pyplot(plt.show())


	col1, col2 = st.columns(2)

	#  Assuming you just bought and held without trading
	with col1:
		st.markdown('**BASELINE:**')
		st.write(f'Return Metric: {"{:,}".format(base_return_metric)}%')
		st.write(f'Compound Annual Growth Rate: {base_cagr_metric}')
		st.write(f'Biggest Drawdown was: {base_dd_metric}%')
		st.write(f'New Balance: ${"{:,}".format(round(start_balance * (base_return_metric/100),2))}')
	
	# Using the Moving Avergage Strategy
	with col2:
		st.markdown('**MOVING AVERAGE STRATEGY:**')
		st.write(f'Return Metric: {"{:,}".format(ma_return_metric)}%')
		st.write(f'Compound Annual Growth Rate: {ma_cagr_metric}')
		st.write(f'Biggest Drawdown was: {ma_dd_metric}%')
		st.write(f'New Balance: ${"{:,}".format(round(start_balance * (ma_return_metric/100),2))}')   

st.write('>Baseline is assuming you were to just buy and hold the stock')