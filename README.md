# Stock Market AlgoTrade
 
This is a software that will use an algorithm to buy and sell stocks. 

## Table of Contents
- [General Info](#general-info)
- [Methodology](#methodology)
- [Technology](#technology)
<!-- - [Improvements](#Improvements) -->

## General Info
I will be using an API to get the price of a certain stock. This way I can calculate my own technical indicators and use them to buy and sell shares using an API. I will be using two APIs. Twelvedata will be used to get the price of the stock and Alpaca will be used to buy and sell stocks. My first goal is to try doing day trades. My plan is to gain 1% a day by doing multiple trades in a day and gaining a few cents per stock per trade. 
* [twelvedata](https://twelvedata.com/) (prices of stocks)
* [Alpaca](https://alpaca.markets/) (buying and selling stocks)

Alpaca has a zero commision fee which lets me do multiple trades in a day while not having each transaction reduce my profits. It also allows paper trading which lets me practice using my algorithm. 

## Methodology

I want to start by using MA (moving average) and EMA (exponential moving average).  I will calculate the opening prices of the stock in order to get real time indicators because using closing prices would result in it being a minute late.

## MA vs EMA

I want to calculate the `MA` and `EMA`. I will be using minutes for my prices and will try *(5 , 7 , 10)* opening prices for my MA and `EMA`. The idea is when my `EMA` and `MA` cross I will do a transaction. I should buy and hold a stock if my `EMA` > `MA`. Once my `EMA` <  `MA` I will sell and wait for `EMA` and `MA` to intersect again. This a simple rule and mostly want to see whether I can work with the API and what are my results after a few days.  

I hope to expand to find new metrics and indicators to implement new methods. 

## Technology 
This project is created with: 
* Python 
* VS Code


## Improvements

[ ] Find a way to use AI or Machine Learning to read the prices and see a trend. I will want to get more metrics nad create a regression model to see what correlates with the price. 
