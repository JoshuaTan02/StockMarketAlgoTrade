from wsgiref import headers
from config import *
import requests,json
import time

APCA_API_BASE_URL="https://paper-api.alpaca.markets/"
ORDERS_URL = APCA_API_BASE_URL+"v2/orders"
ACCOUNT_URL = APCA_API_BASE_URL+"v2/account"

headers = {
    "APCA-API-KEY-ID": alpacaAPI,
    "APCA-API-SECRET-KEY": alpacaSecret
}

def get_account():
    request = requests.get(ACCOUNT_URL,headers = headers)
    return json.loads(request.content)

def get_orders():
    request = requests.get(ORDERS_URL,headers=headers)
    return json.loads(request.content)

def delete_order(id):
    url = ORDERS_URL + "/"+ id
    request = requests.delete(url,headers=headers)
    return request

def get_order(orderID):
    url = ORDERS_URL + "/"+ orderID
    request = requests.get(url,headers=headers)
    return json.loads(request.content)

def buy_order(symbol,qty,side,type,time_in_force):
    body = {
        "symbol":symbol,
        "qty":qty,  # fractional shares
        "side":side,
        "type": type,
        "time_in_force":time_in_force,
    }

    request = requests.post(ORDERS_URL,json =body ,headers = headers)
    return json.loads(request.content)


def updateStats(EMA,MA,buying,orderID):
    #checks if the avg price filled is not null so we know the order was successful

    response = get_order(orderID)


    avgPrice,qty = response["filled_avg_price"],response["qty"]

    while avgPrice is None:
        print("order has not been filled yet waiting antoher 15 seconds")
        time.sleep(15000)
        avgPrice,qty = response["filled_avg_price"],response["qty"]
       
    if buying:
        #this means we bought a stock
        print("Bought stock @: {} and qty: {}".format(avgPrice,qty))
    else:
        #this means we sold the stock
        print("Sold stock @: {} and qty: {}".format(avgPrice,qty))
        orderID = None
    buying = not buying
    
    return calculate_EMA(5),calculate_MA(5),buying,orderID

def calculate_EMA(timeperiod):
    print("")
    return 0
def calculate_MA(timeperiod):
    #take the time period of minutes and calculate the avg from adding up all the prices
    return 0

marketopen = False
buying = True
orderID = None
EMA = calculate_EMA(5)
MA = calculate_MA(5)

while marketopen:

    if buying and orderID is None:
        if EMA > MA:
            response = buy_order('SPY', 1,"buy","market",'gtc')
            buyID = response['id']
            print('submitted buy request')
            buying = False
    else:
        # Now we want to sell the stock when the conditions are met
        if EMA < MA:
            response = buy_order('SPY',1,"sell","market","gtc")
            print('submitted sell request')

    #waits 20 seconds then will check my order if the buyID has been sold or bought
    print("waiting 20 seconds")
    time.sleep(20000)
    EMA,MA,buying,orderID = updateStats(EMA,MA,buying,orderID)
    

