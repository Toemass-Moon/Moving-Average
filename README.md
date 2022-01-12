# Moving Average Strategy For trading Stocks
#### Thomaz Moon

---
## Executive Summary
When it comes to trading stocks, a lot of people have their own ways and ideas on how to "beat the market". Methods can vary from person to person as well as on their risk tolerance. Some people say to just buy and hold a stock for long run, while others try to come up with ways to maximize their profits by trying to "Buy Low and Sell High".

A common and well known strategy is to use the Moving Average to your advantge. The "Moving Average" strat is simply to **sell** when the stock price hits or falls below the moving average line, and **buy** when it goes above.
> You can read more about this idea on [Investopedia's article](https://www.investopedia.com/articles/active-trading/052014/how-use-moving-average-buy-stocks.asp)
  
This short project focuses on testing how well this strategy works. By passing a `stock ticker`, `start` and `end` date, `starting balance`, and `days` for the moving average, you will be able to compare how much you would have made with the moving average VS just buying and holding the stock.  
  

## Basic Structure
There 2 notebooks and 1 python file. The 1st notebook `Moving Average Messing Around.ipynb` was used in order to show how everything was calculated and get some visuals in as well. The 2nd notebook, `Turning the Entire 1st notebook into Functions.ipynb` is taking all the important information from the first notebook and turning it into a one line run function.  

Lastly, the `browser_app.py` file is just a **Streamlit** version of the 2nd notebook, where you can access this project from the browser. [Link Here](https://share.streamlit.io/toemass-moon/moving-average/main/browser_app.py)  
>**Note:** Until a date is passed in formated as `Year/Month/Day` (i.e. 2005/1/1), an error will show up, but after putting in a starting and ending day, the error will go away and the `Run 🏃‍`  button will show up  

<img src='./imgs/moving average streamlit resized.png'>
  

## Reading the Graphs and Information  
| Item 	| Description 	|
|:---:	|:---:	|
| Blue Line (Baseline) 	| The return if you were to just buy and hold the stock. 	|
| Orange Line (MA) 	| The return of the moving average strategy. 	|
| Return Metric 	| What the return rate is. 	|
| Compound Annual Growth Rate 	| Mean annual growth rate of the investment (assuming time span is over a year). 	|
| Biggest Drawdown 	| The largest drop in stock price before recovering. 	|
| New Balance 	| How much you would have ended with given the starting balance. 	|


## Conclusions
Overall, I found that while using the Moving Average would usually result in a significant drop in return, the drawdown was also lower by a significant ammount. This brings up the idea of trade off again. There usually has to be a good balance in whatever we do, whether it's the bias/variance trade off, or the high-risk high return/low-risk low return trade off.  
> An exception I found was `NVDA` with a moving average of 200 days from 2001/1/1 - 2022/1/1. Where it had a higher return (much much higher), as well as a lower Drawdown.  

<img src='./imgs/nvda op.png'>