#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
추가 코딩해야할것 

****  수량이 적으면 거래가 안됨. 잔고모자를때도 거래가 안됨. 
거래할때 거래 amount를 코인수로 체크하는데 이걸 잘 조절하게 해야함 


1. 호가잔량을 체크 
orderbook = gate.fetch_order_book('TRCL/USDT')

#호가 잔량을 확인할때 사용 
#for ask in orderbook['asks']:
#    print(ask[0], ask[1])

#print(balance['BTC']['free']) # free 보유중 used 거래진행중 , total 전체

잔고를 체크하고 나서 코인이 모자른지 알리고~ 
그리고 나서 미체결 물량을 다 제거해줘야함. 
거래소 최소 주문량 이상을 거래하게 해야함. 

"""
import ccxt
import pybithumb
import random

def price_percentage(open_price, close_price):
    rate = round(((close_price - open_price)/open_price)*100 , 2)
        
    return rate

#파이썬 클래스로 변형 / 거래소별로 최저거래량을 계산해야함. 


class trade_crypto:
    def __init__(self, api_key, secret, who):
        self.api_key = api_key
        self.secret = secret
        self.who = who #누구의 계정인지 체크필요 
        self.btc_price = pybithumb.get_current_price("BTC")
        self.eth_price = pybithumb.get_current_price("ETH")
        self.usdt_price = pybithumb.get_current_price("USDT")
        self.config={'apiKey': self.api_key, 'secret': self.secret}
        self.orderbook = {}
    
    
    def mexc_check_balance(self, symbol ):
        exchange = ccxt.mexc(config=self.config)
        balance = exchange.fetch_balance()
        
        
        message = ""
         
        
        try :
            
            #해당코인의 잔고가 있는경우 
            balance_used_coin = round(balance[symbol]['used'],1)#거래진행중
            balance_free_coin = round(balance[symbol]['free'],1)#보유중
            balance_total_coin = round(balance[symbol]['total'],1)#전체
            
            message = "MEXC거래소 "+self.who +" 계정 " +symbol + "<잔고 - 거래진행중 :" +str(balance_used_coin)+\
                "/보유중:" +str(balance_free_coin)+"/총잔고:" +str(balance_total_coin)+">"
        except : 
            
            message = "MEXC거래소 "+self.who +" 계정 " + symbol + "<잔고가 없습니다>"

        return message        
        
        
        
        
    #게이트 거래소 잔고체크         
    def gate_check_balance(self, symbol ):
        exchange = ccxt.gate(config=self.config)
        balance = exchange.fetch_balance()
        
        message = ""
        
        
        try :
            
            #해당코인의 잔고가 있는경우 
            balance_used_coin = round(balance[symbol]['used'],1)#거래진행중
            balance_free_coin = round(balance[symbol]['free'],1)#보유중
            balance_total_coin = round(balance[symbol]['total'],1)#전체
            
            message = "게이트거래소 "+self.who +" 계정 "+ symbol + "<잔고 - 거래진행중 :" +str(balance_used_coin)+ \
                "/보유중:" +str(balance_free_coin)+"/총잔고:" +str(balance_total_coin)+">"
        except : 
            
            message = "게이트거래소 "+self.who +" 계정 "+ symbol + "<잔고가 없습니다>"

        return message     
    
    #비트겟 거래소 잔고체크         
    def bitget_check_balance(self, symbol, password):
        
        self.config={'apiKey': self.api_key, 'secret': self.secret , 'password':password}
        exchange = ccxt.bitget(config=self.config)
        balance = exchange.fetch_balance()
        
        message = ""
        
         
        
        try :
            
            #해당코인의 잔고가 있는경우 
            balance_used_coin = round(balance[symbol]['used'],1)#거래진행중
            balance_free_coin = round(balance[symbol]['free'],1)#보유중
            balance_total_coin = round(balance[symbol]['total'],1)#전체
            
            message = "비트겟거래소 "+self.who +" 계정 "+ symbol + "<잔고 - 거래진행중 :" +str(balance_used_coin)+ \
                "/보유중:" +str(balance_free_coin)+"/총잔고:" +str(balance_total_coin)+">"
        except : 
            
            message = "비트겟거래소 "+self.who +" 계정 "+ symbol + "<잔고가 없습니다>"

        return message   
    
    
    #쿠코인 거래소 잔고체크         
    def kucoin_check_balance(self, symbol, password ):
        self.config={'apiKey': self.api_key, 'secret': self.secret , 'password':password}
        exchange = ccxt.kucoin(config=self.config)
        balance = exchange.fetch_balance()
        
        message = ""
        
        
        try :
            
            #해당코인의 잔고가 있는경우 
            balance_used_coin = round( balance[symbol]['used'],1)#거래진행중
            balance_free_coin = round(balance[symbol]['free'],1)#보유중
            balance_total_coin = round(balance[symbol]['total'],1)#전체
            
            message = "쿠코인거래소 "+self.who +" 계정 "+ symbol + "<잔고 - 거래진행중 :" +str(balance_used_coin)+ "/보유중:" \
                +str(balance_free_coin)+"/총잔고:" +str(balance_total_coin)+">"
        except : 
            
            message = "쿠코인거래소 "+self.who +" 계정 "+ symbol + "<잔고가 없습니다>"

        return message  
    
    
    

    
    
    
    #거래소 매도 / 등락률과 심볼을 인자로 받아서 얼마 이상 가격까지 팔지 않을지 정함. 
    def gate_sell(self, symbol):
        
        
        #시세와 거래량 정보 제공하기 
        self.maket_symbol = symbol + "/USDT"
        gate = ccxt.gateio(config= self.config)
        self.orderbook = gate.fetch_ohlcv(symbol = self.maket_symbol ,timeframe= '1d')
        #print(self.orderbook[-1])   #2번째인자가 시작값 ,  5번째 인자가 현재값 / 마지막 인자가 거래량 / 

        self.rate = price_percentage(self.orderbook[-2][4], self.orderbook[-1][4])
        current_price = round(self.orderbook[-1][4]* self.usdt_price,4)
        
        asks_bids = gate.fetch_order_book(self.maket_symbol)
        
        three_bid = 0
        quant = 0 
        for bid in asks_bids['bids'][0:3]:
            print("3호가" , bid[0] , bid[1])
            three_bid += (bid[0]*bid[1])*self.usdt_price
            quant += bid[1]
        price = asks_bids['bids'][2][0]    
        print("매도가",price)
        quant = round(quant * 0.9 , 1)
        
        #매매 먼저 다 취소해야함 
        cancel_resp = gate.cancel_all_orders(symbol=self.maket_symbol)
        print(cancel_resp)
        #거래
        resp1 = gate.create_limit_sell_order(
            symbol= self.maket_symbol,
            amount=quant,
            price=price
            )
        return resp1
    
    def bitget_sell(self, symbol, password):
        
        
        #시세와 거래량 정보 제공하기 
        self.config={'apiKey': self.api_key, 'secret': self.secret , 'password':password}
        self.maket_symbol = symbol + "/USDT"
        bitget = ccxt.bitget(config= self.config)
        self.orderbook = bitget.fetch_ohlcv(symbol = self.maket_symbol ,timeframe= '1d')
        #print(self.orderbook[-1])   #2번째인자가 시작값 ,  5번째 인자가 현재값 / 마지막 인자가 거래량 / 

        self.rate = price_percentage(self.orderbook[-2][4], self.orderbook[-1][4])
        current_price = round(self.orderbook[-1][4]* self.usdt_price,4)
        
        asks_bids = bitget.fetch_order_book(self.maket_symbol)
        
        three_bid = 0
        quant = 0 
        for bid in asks_bids['bids'][0:3]:
            print("3호가" , bid[0] , bid[1])
            three_bid += (bid[0]*bid[1])*self.usdt_price
            quant += bid[1]
        price = asks_bids['bids'][2][0]    
        print("매도가",price)
        quant = round(quant * 0.9 , 1)
        
        #매매 먼저 다 취소해야함 
        cancel_resp = bitget.cancel_all_orders(symbol=self.maket_symbol)
        print(cancel_resp)
        #거래
        resp1 = bitget.create_limit_sell_order(
            symbol= self.maket_symbol,
            amount=quant,
            price=price
            )
        return resp1
    
    
    #거래소 매수 / 등락률과 심볼을 인자로 받아서 얼마정도 가격까지 매수할지 
    def gate_buy(self, symbol):
        #시세와 거래량 정보 제공하기 
        self.maket_symbol = symbol + "/USDT"
        gate = ccxt.gateio(config= self.config)
        self.orderbook = gate.fetch_ohlcv(symbol = self.maket_symbol ,timeframe= '1d')
        #print(self.orderbook[-1])   #2번째인자가 시작값 ,  5번째 인자가 현재값 / 마지막 인자가 거래량 / 

        self.rate = price_percentage(self.orderbook[-2][4], self.orderbook[-1][4])
        current_price = round(self.orderbook[-1][4]* self.usdt_price,4)
        
        asks_bids = gate.fetch_order_book(self.maket_symbol)
        
        three_ask = 0
        quant = 0 
        for ask in asks_bids['asks'][0:3]:
            print("3호가" , ask[0] , ask[1])
            three_ask += (ask[0]*ask[1])*self.usdt_price
            quant += ask[1]
        
        price = asks_bids['asks'][0][0]    
        print("매도가",price)
        quant = round(quant * 1.5 , 1)
        
        #매매 먼저 다 취소해야함 
        cancel_resp = gate.cancel_all_orders(symbol=self.maket_symbol)
        print(cancel_resp)
        #거래
        resp1 = gate.create_limit_buy_order(
            symbol= self.maket_symbol,
            amount=quant,
            price=price
            )
        return resp1
    
    
    #거래소 자전거래 / 심볼을 인자로 받고 추정거래량을 인자로 받아서 얼마나 거래량 만들지 
    def gate_make_volume(self, symbol, amount):
        
        self.maket_symbol = symbol+'/USDT'
        exchange = ccxt.gate(config=self.config)
        orderbook = exchange.fetch_order_book(self.maket_symbol)
        first_ask = float(orderbook['asks'][0][0]) #최우선 매도호가
        first_bid = float(orderbook['bids'][0][0]) #최우선 매수호가
        
        #매매 먼저 다 취소해야함 
        cancel_resp = exchange.cancel_all_orders(symbol=self.maket_symbol)
        order_price = round((first_ask+first_bid)/2 , 5)
        
        resp1 = exchange.create_limit_sell_order(
            symbol=symbol + '/USDT',
            amount=amount,
            price=order_price
            )

        resp2 = exchange.create_limit_buy_order(
            symbol=symbol+'/USDT',
            amount=amount,
            price=order_price
            )

        print(resp1)
        print(resp2
              )
        
        return resp1, resp2


    #거래소 자전거래 / 심볼을 인자로 받고 추정거래량을 인자로 받아서 얼마나 거래량 만들지 
    def bitget_make_volume(self, symbol, amount, password):
        self.config = {'apiKey': self.api_key, 'secret': self.secret , 'password':password}
        self.maket_symbol = symbol+'/USDT'
        
        
        exchange = ccxt.bitget(config=self.config)
        orderbook = exchange.fetch_order_book(self.maket_symbol)
        first_ask = float(orderbook['asks'][0][0]) #최우선 매도호가
        first_bid = float(orderbook['bids'][0][0]) #최우선 매수호가
        
        #매매 먼저 다 취소해야함 
        cancel_resp = exchange.cancel_all_orders(symbol=self.maket_symbol)
        order_price = round((first_ask+first_bid)/2 , 5)
        
        resp1 = exchange.create_limit_sell_order(
            symbol=symbol + '/USDT',
            amount=amount,
            price=order_price
            )

        resp2 = exchange.create_limit_buy_order(
            symbol=symbol+'/USDT',
            amount=amount,
            price=order_price
            )

        print(resp1)
        print(resp2
              )
        
        return resp1, resp2
    
    #거래소 자전거래 / 심볼을 인자로 받고 추정거래량을 인자로 받아서 얼마나 거래량 만들지 
    def mexc_make_volume(self, symbol, amount):
        
        self.maket_symbol = symbol+'/USDT'
        exchange = ccxt.mexc(config=self.config)
        orderbook = exchange.fetch_order_book(self.maket_symbol)
        first_ask = float(orderbook['asks'][0][0]) #최우선 매도호가
        first_bid = float(orderbook['bids'][0][0]) #최우선 매수호가
        
        #매매 먼저 다 취소해야함 
        cancel_resp = exchange.cancel_all_orders(symbol=self.maket_symbol)
        order_price = round((first_ask+first_bid)/2 , 5)
        
        resp1 = exchange.create_limit_sell_order(
            symbol=symbol + '/USDT',
            amount=amount,
            price=order_price
            )

        resp2 = exchange.create_limit_buy_order(
            symbol=symbol+'/USDT',
            amount=amount,
            price=order_price
            )

        print(resp1)
        print(resp2
              )
        
        return resp1, resp2
    
    #거래소 매수 / 등락률과 심볼을 인자로 받아서 얼마정도 가격까지 매수할지 
    def bitget_buy(self, symbol,password):
        #시세와 거래량 정보 제공하기 
        self.config={'apiKey': self.api_key, 'secret': self.secret , 'password':password}
        self.maket_symbol = symbol + "/USDT"
        bitget = ccxt.bitget(config= self.config)
        self.orderbook = bitget.fetch_ohlcv(symbol = self.maket_symbol ,timeframe= '1d')
        #print(self.orderbook[-1])   #2번째인자가 시작값 ,  5번째 인자가 현재값 / 마지막 인자가 거래량 / 

        self.rate = price_percentage(self.orderbook[-2][4], self.orderbook[-1][4])
        current_price = round(self.orderbook[-1][4]* self.usdt_price,4)
        
        asks_bids = bitget.fetch_order_book(self.maket_symbol)
        
        three_ask = 0
        quant = 0 
        for ask in asks_bids['asks'][0:3]:
            print("3호가" , ask[0] , ask[1])
            three_ask += (ask[0]*ask[1])*self.usdt_price
            quant += ask[1]
        
        price = asks_bids['asks'][0][0]    
        print("매도가",price)
        quant = round(quant * 1.5 , 1)
        
        #매매 먼저 다 취소해야함 
        cancel_resp = bitget.cancel_all_orders(symbol=self.maket_symbol)
        print(cancel_resp)
        #거래
        resp1 = bitget.create_limit_buy_order(
            symbol= self.maket_symbol,
            amount=quant,
            price=price
            )
        return resp1



#mxc lee
api_key = "mx0vglOFnfeQHIsLiN"
secret = "63291ba276ba4a4f8bff20cb2f4d36c4"


#gate_jun_park
api_key_jun_gate = "85653531ddb5cb88b3f5a44bc3866d56"
secret_jun_gate = "d70fa9e3ee560c887bdaf18b09fb3bd7a18b3e466b31a8b45ef3b379ff57f5b0"

#mexc_jun_park
api_key_jun_mexc = "mx0vglkKgiQiUHk4mG"
secret_jun_mexc = "75befaf11815483e900509b8f42e6eb3"

#bitget_jun_park
api_key_jun_bitget = 'bg_cc74451be936606077b11d9611fcf0e4'
secret_jun_bitget = '8a5aa5dba84e4f67797dbb4b900291ed312bb8859accd7be16f7a843c533a0fa'
password_jun_bitget = "Gomdori123123"

#bitget_lee
api_key_lee_bitget = "bg_fd1a84ca80d978d5a1a512fd48cf3a9c"
secret_lee_bitget = "a9b6bbc300b98ef41cf3fedec5901ca3d8115a0e3cd65d43a4a624fe34b81343"
password_lee_bitget = "Roalee891roa"

#bitget_steve

api_key_steve_bitget = "bg_55838a0836f247437604208ba8653f91"
secret_steve_bitget = "ba289996879bcc7147fdfda5f9ef80b6034ca234b0a1169d3d972f5fef0424d3"
password_steve_bitget = "xhdzl3676"

#mexc kim trcl
api_key_kim_mexc = "mx0vglfHEtwpO5AvcI"
secret_kim_mexc = "e83ce8dc979340cab054f673cd2c954d"
    
#gate kimm trcl
api_key_kim_gate = '46a773374cbeca16be160056ad716d26'
secret_kim_gate = '09925c81ad89d4327303c4760b7a2fbf98f66cc3581192f3007ab14c0f5c0926'



'''
#자전거래 게이트아이오 곰도리 
z, y = trade_coin_gate.gate_make_volume("GOMD", 4000)

'''


'''
#게이트 거래소 바이백 매수 
trade_coin_gate = trade_crypto( api_key_jun_gate , secret_jun_gate, "jun_park")
#a1, b1, c1, d1, e1, f1 = trade_coin_gate.gate_check_balance("GOMD")
resp1=trade_coin_gate.gate_buy("GOMD")
print('게이트', resp1)
#비트겟 거래소
trade_coin_bitget = trade_crypto(api_key_jun_bitget, secret_jun_bitget, "jun_park")
resp2=trade_coin_bitget.bitget_buy("GOMD", password_jun_bitget)
print('비트겟' , resp2)

'''

'''
#트리클 자전거래 
gate_trcl_amount = random.randint(10000, 100000)
mexc_trcl_amount = random.randint(10000, 100000)

#mexc 자전거래소 (지금안됨)
trade_coin_mexc = trade_crypto(api_key_kim_mexc, secret_kim_mexc, "kim")
resp1, resp2= trade_coin_mexc.mexc_make_volume("TRCL", mexc_trcl_amount)
mexc_message1 = trade_coin_mexc.mexc_check_balance("USDT")
mexc_message2 = trade_coin_mexc.mexc_check_balance("TRCL")
print(mexc_message1, mexc_message2)


#gate 
trade_coin_gate = trade_crypto(api_key_kim_gate, secret_kim_gate, "kim")
resp1, resp2= trade_coin_gate.gate_make_volume("TRCL", gate_trcl_amount)
gate_message1 = trade_coin_gate.gate_check_balance("USDT")
gate_message2 = trade_coin_gate.gate_check_balance("TRCL")
print(gate_message1, gate_message2)
'''



'''
bitget_message = trade_coin_bitget.bitget_check_balance("USDT", password_jun_bitget)
bitget_message = trade_coin_bitget.bitget_check_balance("GOMD", password_jun_bitget)
'''

















