#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
추가 코딩할 부분 
1. 가격 상승 부분에 대해서 상승하면 상승 / 하락하면 하락했다고 표시 
2. 거래량이 줄었을때 늘어야 한다고 알림 
3. 다른 거래소 추가 


"""

import ccxt
from datetime import datetime
import pybithumb


def price_percentage(open_price, close_price):
    rate = round(((close_price - open_price)/open_price) * 100 , 2)
        
    return rate


class get_crypto_info:
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        
        self.btc_price = pybithumb.get_current_price("BTC")
        self.eth_price = pybithumb.get_current_price("ETH")
        self.usdt_price = pybithumb.get_current_price("USDT")
        
        
    def gateioex(self, symbol): 
        
        #시세와 거래량 정보 제공하기 
        self.maket_symbol = symbol + "/USDT"
        gate = ccxt.gateio()
        self.orderbook = gate.fetch_ohlcv(symbol = self.maket_symbol ,timeframe= '1d')
        print("오류체크최신", self.orderbook)   #2번째인자가 시작값 ,  5번째 인자가 현재값 / 마지막 인자가 거래량 / 
        print('오류체크2-어제가격', self.orderbook[-3][1])
        print('오류체크3-오늘가격', self.orderbook[-1][1])
        print('거래량', self.orderbook[-2][-1])
        
        self.rate = price_percentage(self.orderbook[-3][1], self.orderbook[-1][1])
        current_price = round(self.orderbook[-1][4]* self.usdt_price,4)
        
        volume = format(  round(self.orderbook[-2][-1]* current_price,0)  , ',')
        
        
        #잔고 정보 제공하기  
        gateinfo = "<GATEIO-"+symbol+"시세:"+str(current_price)+"원, 등락률:"+str(self.rate)+"%, 거래량:"+str(volume)+"원>"
                        
        return gateinfo
    
    def gateioex_depth(self, symbol): 
        
        #뎁스체크하기 
        self.maket_symbol = symbol + "/USDT"
        gate = ccxt.gateio()
        self.orderbook = gate.fetch_ohlcv(symbol = self.maket_symbol ,timeframe= '1d')
        #print(self.orderbook[-1])   #2번째인자가 시작값 ,  5번째 인자가 현재값 / 마지막 인자가 거래량 / 
        
        
        self.rate = price_percentage(self.orderbook[-3][1], self.orderbook[-1][1])
        current_price = round(self.orderbook[-1][4]* self.usdt_price,4)
        
        #호가잔량구하는 코드 
        total_ask = 0 #매도호가
        total_bid = 0 #매수호가 
        three_ask = 0
        three_bid = 0
        quant =0
        asks_bids = gate.fetch_order_book(self.maket_symbol)
        for ask in asks_bids['asks']:
            print("총" , ask[0] , ask[1])
            total_ask += (ask[0]*ask[1])*self.usdt_price
        for ask in asks_bids['asks'][0:3]:
            print("3호가" , ask[0] , ask[1])
            three_ask += (ask[0]*ask[1])*self.usdt_price
        
        for bid in asks_bids['bids']:
            print("총" , bid[0], bid[1])
            total_bid += (bid[0]*bid[1])*self.usdt_price
        for bid in asks_bids['bids'][0:3]:
            print("3호가" , bid[0] , bid[1])
            three_bid += (bid[0]*bid[1])*self.usdt_price
            quant += bid[1]
            
        total_ask = format(round(total_ask,1), ',')
        total_bid = format(round(total_bid,1), ',')
        three_ask = format(round(three_ask,1), ',')
        three_bid = format(round(three_bid,1), ',')
        print(total_ask)
        print(total_bid)
        
        volume = format(  round(self.orderbook[-2][-1]* current_price,0)  , ',')
        
        
        gateinfo = "📢GATEIO\n"+symbol+"시세\n"+str(current_price)+"원, 등락률:"+str(self.rate)+"%, 거래량:"+str(volume)+"원\n"\
                    + "📣  호가분석\n" + "📉 총매도호가:" + str(total_ask) + \
                    "원\n" + "📈 총매수호가:" + str(total_bid) + "원\n" \
                        +"📉 최우선매도3호가:" + \
                        str(three_ask) + '원\n'\
                            + "📈 최우선매수3호가:" + str(three_bid) + "원"
                    
                    
        #📈📉
        
        return gateinfo , quant
    
    
    
    def bitgetex(self, symbol):
        #시세와 거래량 정보 제공하기 
        
        self.maket_symbol = symbol + "/USDT"
        bitget = ccxt.bitget()
        self.orderbook = bitget.fetch_ohlcv(symbol = self.maket_symbol ,timeframe= '1d')
        #print(self.orderbook[-1])   #2번째인자가 시작값 ,  5번째 인자가 현재값 / 마지막 인자가 거래량 / 
        print(self.orderbook)
        self.rate = price_percentage(self.orderbook[-3][1], self.orderbook[-1][4])
        current_price = round(self.orderbook[-1][4]* self.usdt_price,4)
        
        volume = format(  round(self.orderbook[-1][-1]* current_price,0)  , ',')
        
        #잔고 정보 제공하기  
        bitgetinfo = "<BITGET-"+symbol+"시세:"+str(current_price)+"원, 등락률:"+str(self.rate)+"%, 거래량:"+str(volume)+"원>"
                        
        return bitgetinfo
        
    def bitgetex_depth(self, symbol): 
        
        #뎁스체크하기 
        self.maket_symbol = symbol + "/USDT"
        bitget = ccxt.bitget()
        self.orderbook = bitget.fetch_ohlcv(symbol = self.maket_symbol ,timeframe= '1d')
        #print(self.orderbook[-1])   #2번째인자가 시작값 ,  5번째 인자가 현재값 / 마지막 인자가 거래량 / 
        
        self.rate = price_percentage(self.orderbook[-3][1], self.orderbook[-1][4])
        current_price = round(self.orderbook[-1][4]* self.usdt_price,4)
        
        #호가잔량구하는 코드 
        total_ask = 0 #매도호가
        total_bid = 0 #매수호가 
        three_ask = 0
        three_bid = 0
        quant = 0
        asks_bids = bitget.fetch_order_book(self.maket_symbol)
        for ask in asks_bids['asks']:
            print("총" , ask[0] , ask[1])
            total_ask += (ask[0]*ask[1])*self.usdt_price
        for ask in asks_bids['asks'][0:3]:
            print("3호가" , ask[0] , ask[1])
            three_ask += (ask[0]*ask[1])*self.usdt_price
        
        for bid in asks_bids['bids']:
            print("총" , bid[0], bid[1])
            total_bid += (bid[0]*bid[1])*self.usdt_price
        for bid in asks_bids['bids'][0:3]:
            print("3호가" , bid[0] , bid[1])
            three_bid += (bid[0]*bid[1])*self.usdt_price
            quant += bid[1]
            
        total_ask = format(round(total_ask,1), ',')
        total_bid = format(round(total_bid,1), ',')
        three_ask = format(round(three_ask,1), ',')
        three_bid = format(round(three_bid,1), ',')
        
        
        volume = format(  round(self.orderbook[-1][-1]* current_price,0)  , ',')
        
        
        bitgetinfo = "📣BITGET \n"+symbol+"시세\n"+str(current_price)+"원, 등락률:"+str(self.rate)+"%, 거래량:"+str(volume)+"원\n"\
                    + "📣  호가분석\n" + "📉 총매도호가:" + str(total_ask) + \
                    "원\n" + "📈 총매수호가:" + str(total_bid) + "원\n" \
                        +"📉 최우선매도3호가:" + \
                        str(three_ask) + '원\n'\
                            + "📈 최우선매수3호가:" + str(three_bid) + "원"
                    
                    
        #📈📉
        
        return bitgetinfo, quant
        
    def mexcex(self, symbol):
    
        #시세와 거래량 정보 제공하기 
        self.maket_symbol = symbol + "/USDT"
        mexc = ccxt.mexc()
        self.orderbook = mexc.fetch_ohlcv(symbol = self.maket_symbol ,timeframe= '1d')
        #print(self.orderbook[-1])   #2번째인자가 시작값 ,  5번째 인자가 현재값 / 마지막 인자가 거래량 / 

        self.rate = price_percentage(self.orderbook[-2][4], self.orderbook[-1][4])
        current_price = round(self.orderbook[-1][4]* self.usdt_price,4)
        
        volume = format(  round(self.orderbook[-1][-1]* current_price,0)  , ',')
        
        
        #잔고 정보 제공하기  
        mexcinfo = "<MEXC-"+symbol+"시세:"+str(current_price)+"원, 등락률:"+str(self.rate)+"%, 거래량:"+str(volume)+"원>"
                        
        return mexcinfo
    
        
    
    def kucoinex(self, symbol):
    
        #시세와 거래량 정보 제공하기 
        self.maket_symbol = symbol + "/USDT"
        mexc = ccxt.kucoin()
        self.orderbook = mexc.fetch_ohlcv(symbol = self.maket_symbol ,timeframe= '1d')
        #print(self.orderbook[-1])   #2번째인자가 시작값 ,  5번째 인자가 현재값 / 마지막 인자가 거래량 / 

        self.rate = price_percentage(self.orderbook[-2][4], self.orderbook[-1][4])
        current_price = round(self.orderbook[-1][4]* self.usdt_price,4)
        
        volume = format(  round(self.orderbook[-1][-1]* current_price,0)  , ',')
        
        
        #잔고 정보 제공하기  
        kucoininfo = "<쿠코인-"+symbol+"시세:"+str(current_price)+"원, 등락률:"+str(self.rate)+"%, 거래량:"+str(volume)+"원>"
                        
        return kucoininfo
        
    
    def kucoinex_depth(self, symbol): 
        
        #뎁스체크하기 
        self.maket_symbol = symbol + "/USDT"
        kucoin = ccxt.kucoin()
        self.orderbook = kucoin.fetch_ohlcv(symbol = self.maket_symbol ,timeframe= '1d')
        #print(self.orderbook[-1])   #2번째인자가 시작값 ,  5번째 인자가 현재값 / 마지막 인자가 거래량 / 
        
        self.rate = price_percentage(self.orderbook[-2][4], self.orderbook[-1][4])
        current_price = round(self.orderbook[-1][4]* self.usdt_price,4)
        
        #호가잔량구하는 코드 
        total_ask = 0 #매도호가
        total_bid = 0 #매수호가 
        three_ask = 0
        three_bid = 0
        quant = 0
        asks_bids = kucoin.fetch_order_book(self.maket_symbol)
        for ask in asks_bids['asks']:
            print("총" , ask[0] , ask[1])
            total_ask += (ask[0]*ask[1])*self.usdt_price
        for ask in asks_bids['asks'][0:3]:
            print("3호가" , ask[0] , ask[1])
            three_ask += (ask[0]*ask[1])*self.usdt_price
        
        for bid in asks_bids['bids']:
            print("총" , bid[0], bid[1])
            total_bid += (bid[0]*bid[1])*self.usdt_price
        for bid in asks_bids['bids'][0:3]:
            print("3호가" , bid[0] , bid[1])
            three_bid += (bid[0]*bid[1])*self.usdt_price
            quant += bid[1]
            
        total_ask = format(round(total_ask,1), ',')
        total_bid = format(round(total_bid,1), ',')
        three_ask = format(round(three_ask,1), ',')
        three_bid = format(round(three_bid,1), ',')
        
        
        volume = format(  round(self.orderbook[-1][-1]* current_price,0)  , ',')
        
        
        kucoininfo = "📣KUCOIN \n"+symbol+"시세\n"+str(current_price)+"원, 등락률:"+str(self.rate)+"%, 거래량:"+str(volume)+"원\n"\
                    + "📣  호가분석\n" + "📉 총매도호가:" + str(total_ask) + \
                    "원\n" + "📈 총매수호가:" + str(total_bid) + "원\n" \
                        +"📉 최우선매도3호가:" + \
                        str(three_ask) + '원\n'\
                            + "📈 최우선매수3호가:" + str(three_bid) + "원"
                    
                    
        #📈📉
        
        return kucoininfo, quant    
    
    
    
        
        
    def bybitex(self):
        
        
        return
   
    
#📢📣☑️⬆️⬇️💲🔤📈📉💸⌛️🔈🆕📣🔥💥   
    

   
key = "85653531ddb5cb88b3f5a44bc3866d56"
secret = "d70fa9e3ee560c887bdaf18b09fb3bd7a18b3e466b31a8b45ef3b379ff57f5b0"

#bitget_lee
api_key_lee_bitget = "bg_fd1a84ca80d978d5a1a512fd48cf3a9c"
secret_lee_bitget = "a9b6bbc300b98ef41cf3fedec5901ca3d8115a0e3cd65d43a4a624fe34b81343"
password_lee_bitget = "Roalee891roa"


get = get_crypto_info(key, secret)
gateinfo = get.gateioex("GOMD")
print(gateinfo)


get = get_crypto_info(api_key_lee_bitget, secret_lee_bitget)
bitgetinfo = get.bitgetex("GOMD")
print(bitgetinfo)



'''
#쿠코인 호가 분석 
get = get_crypto_info('661e5bbe482ffe0001c51f42', '3b436ccf-f399-446d-b48c-4ab606a8a419')
kucoininfo, quant = get.kucoinex_depth("EGAME")
print(kucoininfo, quant)


'''











