# Stock Market AlgoTrade
 
This is a software that will use an algorithm to buy and sell stocks. 

## Table of Contents
- [General Info](#general-info)
- [Methodology](#methodology)
- [Technology](#technology)
<!-- - [Improvements](#Improvements) -->

## General Info
I will be using an API to get the price of a certain stock. This way I can calculate my own technical indicators and use them to buy and sell shares using an API. I will be using two APIs. Polygon will be used to get the price of the stock and Alpaca will be used to buy and sell stocks. My first goal is to try doing day trades. My plan is to gain 1% a day by doing multiple trades in a day and gaining a few cents per stock per trade. 
* [Polygon.io](https://polygon.io/) (prices of stocks)
* [Alpaca](https://alpaca.markets/) (buying and selling stocks)

Alpaca has a zero commision fee which lets me do multiple trades in a day while not having each transaction reduce my profits. It also allows paper trading which lets me practice using my algorithm. 

## Methodology

I want to start by using MA (moving average) and EMA (exponential moving average).  I will calculate the opening prices of the stock in order to get real time indicators because using closing prices would result in it being a minute late.

## Technology 
This project is created with: 
* Python 
* VS Code


<!-- ## Improvements -->

