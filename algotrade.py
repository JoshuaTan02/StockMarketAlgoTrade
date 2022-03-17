from wsgiref import headers


polygonAPI = "OBeyZxQWRg8yHWTPhzpunAj2vlz2MhPT"
alpacaAPI = "PK7DB6BYMCF603DND7F7"
alpacaSecret = "MDthzYcXKXpJNiWPrtx4RxNtRycpUt3xEPZXYHJG"

APCA_API_BASE_URL="https://paper-api.alpaca.markets/"

ORDERS_URL = APCA_API_BASE_URL+"v2/orders"

headers = {
    "APCA_API_KEY_ID": alpacaAPI,
    "APCA_API_SECRET_KEY": alpacaSecret
}
def order(symbol,qty,side,type,time_in_force):
    body = {
        "symbol":symbol,
        "qty":qty,  # fractional shares
        "side":side,
        "type":type,
        "time_in_force":time_in_force,
    }
api.submit_order(
    symbol='SPY',
    qty=1.5,  # fractional shares
    side='buy',
    type='market',
    time_in_force='day',
)