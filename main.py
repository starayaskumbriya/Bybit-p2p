import telegram_send
import time
import asyncio
import requests
url = "https://api2.bybit.com/fiat/otc/item/online"

data = {
    "userId":"",
    "tokenId":"USDT",
    "currencyId":"BYN",
    "payment":[],
    "side":"1",
    "size":"10",
    "page":"1",
    "amount":"",
    "authMaker":False,
    "canTrade":False
}

normalPrice = 3.22
while(1):
    responce = requests.post(url, json=data)
    result = responce.json()['result']
    bestPrice = result['items'][0]['price']
    if(float(bestPrice) <= normalPrice):
        asyncio.get_event_loop().run_until_complete(telegram_send.send(messages=['надо брать! цена сейчас '+ bestPrice +'р']))
    time.sleep(10)


