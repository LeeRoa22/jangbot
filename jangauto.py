#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:42:48 2024

@author: leesnotebook
"""

# 자전거래 계정임
import trade
import telegram
import asyncio
import pybithumb
import nest_asyncio 
import ccxt
from datetime import datetime

#여러가지 텔레그램 관련 모듈 불러오기
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext,ApplicationBuilder, \
    ContextTypes
import logging
import telegram.ext.filters as filters
import os
from telegram import ForceReply
import getinfo
import trade


import time

# 관련 패키지 및 모듈 import
import schedule
import time
import datetime
import random


#리 자산관리봇 
token_lee = "7116461299:AAFaNgpU3h-XeY9LT1AjTkU2WCJXqYViISE" #리봇
token_will = "7107282295:AAE_Lp6zGERrM08D18_SF5GhMy9NYrBs1eo"#윌봇
token_jang = "7166675840:AAHkxm00HPqU3-X5-wGw5GMWvJDk-7q-ETE" #장봇
token_chikyu = "6448341216:AAH_ITMeAEsasiSyb0-P4uLPfJdyaCl7tpc"#치규봇

#리브라더스
chat_id_leeh = '1039120014' #lee hid
chat_id_leeb = '1615288066' #lee bid
chat_id_ray = '898698104' #레이몬

chat_id_will = '466171409' #이수한 윌 
chat_id_jang = '583462302' #장건영
chat_id_chikyu = '428874505'#배치규

# gate_jun_park
api_key_jun_gate = "85653531ddb5cb88b3f5a44bc3866d56"
secret_jun_gate = "d70fa9e3ee560c887bdaf18b09fb3bd7a18b3e466b31a8b45ef3b379ff57f5b0"

# mexc_jun_park
api_key_jun_mexc = "mx0vglkKgiQiUHk4mG"
secret_jun_mexc = "75befaf11815483e900509b8f42e6eb3"

# bitget_jun_park
api_key_jun_bitget = 'bg_cc74451be936606077b11d9611fcf0e4'
secret_jun_bitget = '8a5aa5dba84e4f67797dbb4b900291ed312bb8859accd7be16f7a843c533a0fa'
password_jun_bitget = "Gomdori123123"


#jang

api_key_jang_gate = "cc53ebc7532f2729657f99f14c176156"
secret_jang_gate = "dfb6283c811924a41fe471b4182299dde999bfeece0e363f56bdc946c9deeaf2"

api_key_jang_bitget = "bg_211e5f732502d90b6b42c3a81e471695"
secret_jang_bitget=  "21180681ac8f197da6340329da2b043ffd9a2e0b9f5edbb5a499fba8a39c3c69"
password_jang_bitget = "Rhaehfl123"

api_key_jang_kucoin = "6623c3bb6b8d6e0001681855"
secret_jang_kucoin = "309d758b-1e1a-4bee-be3c-92034eb286e1"
password_jang_kucoin = "Rhaehfl123"
#lee

#mxc lee
api_key = "mx0vglOFnfeQHIsLiN"
secret = "63291ba276ba4a4f8bff20cb2f4d36c4"

#bitget_lee
api_key_lee_bitget = "bg_fd1a84ca80d978d5a1a512fd48cf3a9c"
secret_lee_bitget = "a9b6bbc300b98ef41cf3fedec5901ca3d8115a0e3cd65d43a4a624fe34b81343"
password_lee_bitget = "Roalee891roa"

#jun_park

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

#kucoin_jun_park
api_key_jun_kucoin = "6623844eb4dd030001f9699e"
secret_jun_kucoin = "8c2d18cb-3bdf-48b2-9738-5dada82502c7"
password_jun_kucoin = "Gomdori123123"


#steve

#gate_steve
api_key_steve_gate = "898dc2583f517f7424d72957dbd1a0af"
secret_steve_gate = "edcbd4ba92b30bb3867bcb7690b8e45d878179b94f8e09ec138e89f52d11511a"

#mexc_steve
api_key_steve_mexc = "mx0vgla9bQMju4MJ4x"
secret_steve_mexc = "461f7df10a6f44b9b3e040fa3fe61b0c"

#bitget_steve

api_key_steve_bitget = "bg_55838a0836f247437604208ba8653f91"
secret_steve_bitget = "ba289996879bcc7147fdfda5f9ef80b6034ca234b0a1169d3d972f5fef0424d3"
password_steve_bitget = "xhdzl3676"

#kucoin_steve
api_key_steve_kucoin = "6623204b09083300017d1f94"
secret_steve_kucoin = "8b1df306-536f-401b-b7e2-f92e16df05b7"
password_steve_kucoin = "xhdzl3676"


#huu1 

#gate_huu1
api_key_huu1_gate = "5955fc1ff82c1e8a80da74ab49251a44"
secret_huu1_gate = "38cbb091b9d849a0879cd4e3773a203df8a658ceea831191f832e679cc1c9e3b"

#mexc_huu1

#bitget_huu1
api_key_huu1_bitget = "bg_a96477d6ac360ffb2378d669dc1ec194"
secret_huu1_bitget = "d347760017d1c837fee13654a80d4bd2053c12774f473f4f81439c708572f431"
password_huu1_bitget = "12121983"

#kucoin_huu1
api_key_huu1_kucoin = "66233e5e1b0aee00017619da"
secret_huu1_kucoin = "220715ad-2a16-46ed-8793-5ea2793e37ed"
password_huu1_kucoin = "12121983"




#huu2

#gate_huu2
api_key_huu2_gate = "e863c959e24b66f0260deac37a653455"
secret_huu2_gate = "8798d64575f895e8bc2511bdee8d2f2d43a5d1df765d3e7f399d64324f5349e7"

#mexc_huu2
api_key_huu2_mexc = "mx0vglKlH89e11h9i1"
secret_huu2_mexc = "fc4c6bc772124c29b925286d3582c106"

#bitget_huu2
api_key_huu2_bitget = "bg_11c9eab82aaa80ba4a6cdac5c134ab1e"
secret_huu2_bitget = "06f8d8b9dfc39ee9442d69f20ac21605190573d269dd3236205e15d9443bb46e"
password_huu2_bitget="12121983"

#kucoint_huu2
api_key_huu2_kucoin = "66233aa1482ffe0001d1f89c"
secret_huu2_kucoin = "a763e83f-1cc3-4df2-b7a9-7bfddd66bf56"
password_huu2_kucoin = "12121983"

#huu3

#gate_huu3
api_key_huu3_gate = "9e9d65acbcdb7e25c188ad29666b72a0"
secret_huu3_gate = "32c1b45e3646a94cdeee23175fa7df09e3d4eec257b93e70fc46b33284fc7e40"

#mexc_huu3
api_key_huu3_mexc = ""
secret_huu3_mexc = ""

#bitget_huu3
api_key_huu3_bitget = "bg_94de5475c3012f4c23a3b0e7733a9848"
secret_huu3_bitget = "cd9b80708599e53eb9881d72bbb3819e5e2b012e2ef19b46b135602059703029"
password_huu3_bitget = "12121983"

#kucoint_huu3
api_key_huu3_kucoin = "66233f3c9a1d640001aaef3a"
secret_huu3_kucoin = "fb843274-f05b-460b-8024-7e1f8c6fa3d3"
password_huu3_kucoin = "12121983"



#mexc kim trcl
api_key_kim_mexc = "mx0vglfHEtwpO5AvcI"
secret_kim_mexc = "e83ce8dc979340cab054f673cd2c954d"
    
#gate kimm trcl
api_key_kim_gate = '46a773374cbeca16be160056ad716d26'
secret_kim_gate = '09925c81ad89d4327303c4760b7a2fbf98f66cc3581192f3007ab14c0f5c0926'



nest_asyncio.apply()


async def main1(chat_id, token, message): #자산 알림봇

    
    bot = telegram.Bot(token = token)
    await bot.send_message(chat_id, message )

#📢📣☑️⬆️⬇️💲🔤📈📉💸⌛️🔈🆕📣🔥💥

# 실행할 함수 선언
def self_trade():
    print("self_trade 스케쥴러")
    #곰도리 자전거래 
    '''
    # amount 지정
    gate_gomd_amount = random.randint(10000, 100000)
    bitget_gomd_amount = random.randint(10000, 100000)

    trade_gate = trade.trade_crypto(api_key=api_key_jang_gate, secret=secret_jang_gate, who="jang")
    resp1, resp2 = trade_gate.gate_make_volume("GOMD", gate_gomd_amount)

    print("게이트거래완료")

    trade_bitget = trade.trade_crypto(api_key=api_key_jang_bitget, secret=secret_jang_bitget, who="jang")
    resp1, resp2 = trade_bitget.bitget_make_volume("GOMD", gate_gomd_amount, password_jang_bitget)

    print("비트겟거래완료")
    '''
    #트리클 자전거래 
    gate_trcl_amount = random.randint(10000, 100000)
    mexc_trcl_amount = random.randint(10000, 100000)
    
    #mexc 자전거래소 (지금안됨)
    trade_coin_mexc = trade.trade_crypto(api_key_kim_mexc, secret_kim_mexc, "kim")
    resp1, resp2= trade_coin_mexc.mexc_make_volume("TRCL", mexc_trcl_amount)
    mexc_message1 = trade_coin_mexc.mexc_check_balance("USDT")
    mexc_message2 = trade_coin_mexc.mexc_check_balance("TRCL")
    print(mexc_message1, mexc_message2)

    
    #gate 
    trade_coin_gate = trade.trade_crypto(api_key_kim_gate, secret_kim_gate, "kim")
    resp1, resp2= trade_coin_gate.gate_make_volume("TRCL", gate_trcl_amount)
    gate_message1 = trade_coin_gate.gate_check_balance("USDT")
    gate_message2 = trade_coin_gate.gate_check_balance("TRCL")
    print(gate_message1, gate_message2)
    print('트리클거래량 돌아감')
    # 매도 또는 매수 전략
    

def trade_coin():
    # 매수시에
    
    #게이트 거래소 
    trade_coin_gate =trade.trade_crypto( api_key_jun_gate , secret_jun_gate, "jun_park")
    #a1, b1, c1, d1, e1, f1 = trade_coin_gate.gate_check_balance("GOMD")
    resp1=trade_coin_gate.gate_buy("GOMD")
    print('게이트', resp1)
    #비트겟 거래소
    trade_coin_bitget = trade.trade_crypto(api_key_jun_bitget, secret_jun_bitget, "jun_park")
    resp2=trade_coin_bitget.bitget_buy("GOMD", password_jun_bitget)
    print('비트겟' , resp2)
    # 매도시에
    
    
    return None


def alarm_balance():
    #게이트 거래소 jang
    trade_coin_gate = trade.trade_crypto( api_key_jang_gate , secret_jang_gate, "jang")
    gate_message0 = trade_coin_gate.gate_check_balance("GOMD")
    gate_message00 = trade_coin_gate.gate_check_balance("USDT")


    #게이트 거래소 준팍
    trade_coin_gate = trade.trade_crypto( api_key_jun_gate , secret_jun_gate, "jun_park")

    gate_message1 = trade_coin_gate.gate_check_balance("GOMD")
    gate_message2 = trade_coin_gate.gate_check_balance("USDT")

    #게이트 거래소 스티브 
    trade_coin_gate = trade.trade_crypto( api_key_steve_gate , secret_steve_gate, "steve")

    gate_message3 = trade_coin_gate.gate_check_balance("GOMD")
    gate_message4 = trade_coin_gate.gate_check_balance("USDT")

    #게이트 거래소 huu1
    trade_coin_gate = trade.trade_crypto( api_key_huu1_gate , secret_huu1_gate, "huu1")

    gate_message5 = trade_coin_gate.gate_check_balance("GOMD")
    gate_message6 = trade_coin_gate.gate_check_balance("USDT")

    #게이트 거래소 huu2
    trade_coin_gate = trade.trade_crypto( api_key_huu2_gate , secret_huu2_gate, "huu2")
    gate_message7 = trade_coin_gate.gate_check_balance("GOMD")
    gate_message8 = trade_coin_gate.gate_check_balance("USDT")
    #게이트 거래소 huu3
    trade_coin_gate = trade.trade_crypto( api_key_huu3_gate , secret_huu3_gate, "huu3")
    gate_message9 = trade_coin_gate.gate_check_balance("GOMD")
    gate_message10 = trade_coin_gate.gate_check_balance("USDT")

    #mexc 준팍 거래소
    trade_coin_mexc = trade.trade_crypto(api_key_jun_mexc, secret_jun_mexc, "jun_park")
    mexc_message1 = trade_coin_mexc.mexc_check_balance("USDT")
    mexc_message2 = trade_coin_mexc.mexc_check_balance("GOMD")


    #mexc 스티브
    trade_coin_mexc = trade.trade_crypto(api_key_steve_mexc, secret_steve_mexc, "steve")

    mexc_message3 = trade_coin_mexc.mexc_check_balance("USDT")
    mexc_message4 = trade_coin_mexc.mexc_check_balance("GOMD")

    #mexc huu2 거래소
    trade_coin_mexc = trade.trade_crypto(api_key_huu2_mexc, secret_huu2_mexc, "huu2")
    mexc_message5 = trade_coin_mexc.mexc_check_balance("USDT")
    mexc_message6 = trade_coin_mexc.mexc_check_balance("GOMD")

    '''
    #mexc huu3 거래소 지금 없음 
    trade_coin_mexc = trade.trade_crypto(api_key_huu3_mexc, secret_huu3_mexc, "huu3")
    mexc_message7 = trade_coin_mexc.mexc_check_balance("USDT")
    mexc_message8 = trade_coin_mexc.mexc_check_balance("GOMD")
    '''
    trade_coin_bitget = trade.trade_crypto(api_key_jang_bitget, secret_jang_bitget, "jang")
    bitget_message0 = trade_coin_bitget.bitget_check_balance("USDT", password_jang_bitget)
    bitget_message00 = trade_coin_bitget.bitget_check_balance("GOMD", password_jang_bitget)

    #비트겟 거래소 준팍
    trade_coin_bitget = trade.trade_crypto(api_key_jun_bitget, secret_jun_bitget, "jun_park")
    bitget_message1 = trade_coin_bitget.bitget_check_balance("USDT", password_jun_bitget)
    bitget_message2 = trade_coin_bitget.bitget_check_balance("GOMD", password_jun_bitget)
    #비트겟 거래소 스티브 
    trade_coin_bitget = trade.trade_crypto(api_key_steve_bitget, secret_steve_bitget, "steve")
    bitget_message3 = trade_coin_bitget.bitget_check_balance("USDT", password_steve_bitget)
    bitget_message4 = trade_coin_bitget.bitget_check_balance("GOMD", password_steve_bitget)


    #비트겟 거래소 huu1 지금 안됨 
    trade_coin_bitget = trade.trade_crypto(api_key_huu1_bitget, secret_huu1_bitget, "huu1")
    bitget_message5 = trade_coin_bitget.bitget_check_balance("USDT", password_huu1_bitget)
    bitget_message6 = trade_coin_bitget.bitget_check_balance("GOMD", password_huu1_bitget)


    #비트겟 거래소 huu2
    trade_coin_bitget = trade.trade_crypto(api_key_huu2_bitget, secret_huu2_bitget, "huu2")
    bitget_message7 = trade_coin_bitget.bitget_check_balance("USDT", password_huu2_bitget)
    bitget_message8 = trade_coin_bitget.bitget_check_balance("GOMD", password_huu2_bitget)
    #비트겟 거래소 huu3
    trade_coin_bitget = trade.trade_crypto(api_key_huu3_bitget, secret_huu3_bitget, "huu3")
    bitget_message9 = trade_coin_bitget.bitget_check_balance("USDT", password_huu3_bitget)
    bitget_message10 = trade_coin_bitget.bitget_check_balance("GOMD", password_huu3_bitget)

    #쿠코인 거래소 장
    trade_coin_kucoin = trade.trade_crypto(api_key_jang_kucoin, secret_jang_kucoin, "jang")
    kucoin_message0 = trade_coin_kucoin.kucoin_check_balance("USDT", password_jang_kucoin)
    kucoin_message00 = trade_coin_kucoin.kucoin_check_balance("GOMD", password_jang_kucoin)
    #쿠코인 거래소 준팍
    trade_coin_kucoin = trade.trade_crypto(api_key_jun_kucoin, secret_jun_kucoin, "jun_park")
    kucoin_message1 = trade_coin_kucoin.kucoin_check_balance("USDT", password_jun_kucoin)
    kucoin_message2 = trade_coin_kucoin.kucoin_check_balance("GOMD", password_jun_kucoin)

    #쿠코인 거래소 steve
    trade_coin_kucoin = trade.trade_crypto(api_key_steve_kucoin, secret_steve_kucoin, "steve")
    kucoin_message3 = trade_coin_kucoin.kucoin_check_balance("USDT", password_steve_kucoin)
    kucoin_message4 = trade_coin_kucoin.kucoin_check_balance("GOMD", password_steve_kucoin)
    #쿠코인 거래소 huu1
    trade_coin_kucoin = trade.trade_crypto(api_key_huu1_kucoin, secret_huu1_kucoin, "huu1")
    kucoin_message5 = trade_coin_kucoin.kucoin_check_balance("USDT", password_huu1_kucoin)
    kucoin_message6 = trade_coin_kucoin.kucoin_check_balance("GOMD", password_huu1_kucoin)
    
    
    
    
    
    get = getinfo.get_crypto_info(api_key_jang_gate, secret_jang_gate)
    gate_gomd = get.gateioex("GOMD")
    get = getinfo.get_crypto_info(api_key_jang_bitget, secret_jang_bitget)
    bitget_gomd = get.bitgetex("GOMD")
    
    
    message_jang = "🆕"+ gate_gomd + "\n🆕"+ bitget_gomd + "\n    💰잔고현황\n📣"  + gate_message0 + "\n📣"+gate_message00 + \
         gate_message1 + "\n📣"+gate_message2+\
            "\n📣"+gate_message3 + "\n📣"+gate_message4 +  "\n📣"+gate_message5 + "\n📣"+gate_message6 + \
            "\n📣"+gate_message7 + "\n📣"+gate_message8 +  "\n📣"+gate_message9 + "\n📣"+gate_message10 +\
            "\n📣"+mexc_message1 + \
             "\n📣"+mexc_message2 + "\n📣" + mexc_message3 + \
                 "\n📣" + mexc_message4 + "\n📣" + mexc_message5+ "\n📣" + mexc_message6+\
                     "\n📣"+bitget_message0 + "\n📣"+bitget_message00 + "\n📣"+bitget_message1 + "\n📣"+bitget_message2 + \
                      "\n📣"+bitget_message3+ "\n📣"+bitget_message4 + "\n📣"+bitget_message5 +"\n📣"+bitget_message6 +\
                          "\n📣"+bitget_message7 +"\n📣"+bitget_message8 +"\n📣"+bitget_message9 +"\n📣"+bitget_message10 +\
                          "\n📣"+kucoin_message0+ "\n📣"+kucoin_message00+"\n📣"+kucoin_message1+ "\n📣"+kucoin_message2+"\n📣"+kucoin_message3+ \
                          "\n📣"+kucoin_message4+ "\n📣"+kucoin_message5+ "\n📣"+kucoin_message6+  \
                         "\n\n  📈정산현황 : 업데이트 예정✅"
    nest_asyncio.apply()
    #장
    asyncio.run(main1(chat_id_jang, token_jang, message_jang))
    asyncio.run(main1(chat_id_leeb, token_jang, message_jang))
    asyncio.run(main1(chat_id_ray, token_jang, message_jang))
    
    return None

    
def alarm_depth():
    
    get_gate = getinfo.get_crypto_info(api_key_jun_gate, secret_jun_gate)
    gateinfo, gate_quant = get_gate.gateioex_depth("GOMD")

    get_bitget = getinfo.get_crypto_info(api_key_jun_bitget, secret_jun_bitget)
    bitgetinfo , bitget_quant = get_bitget.bitgetex_depth("GOMD")

    #호가와 잔고를 분석해서 알림 날려주면됨. 
    message = gateinfo + "\n\n" + bitgetinfo 

    print(gate_quant)
    print(bitget_quant)
    nest_asyncio.apply()
    asyncio.run(main1(chat_id_jang, token_jang, message))
    asyncio.run(main1(chat_id_leeb, token_jang, message))
    asyncio.run(main1(chat_id_ray, token_jang, message))
    
    
    return None




# 실행 주기 설정
# schedule1 = schedule.every(5).seconds.do(printing) # 초

schedule.every(4).minutes.do(self_trade)  # 분
schedule.every(30).minutes.do(trade_coin)  # 분
schedule.every(3).hours.do(alarm_balance) # 시
schedule.every(1).hours.do(alarm_depth) # 시
# schedule.every(3).days.do(printing) # 일
# schedule.every(3).weeks.do(printing) # 주
# schedule.every(1).days.at("19:08").do(self_trade)
count = 0


trade_coin()
alarm_balance()
alarm_depth()
self_trade()

# 스케줄 시작 - 루프
while True:
    # 모든 schedule 기능 실행
    schedule.run_pending()
    now = datetime.datetime.now()
    print(now, '감시중')
    time.sleep(10)
    
    # 모든 스케줄 3번 넘게 시행시 스케줄 종료
    count = count + 1
    print(count)
    if count > 10000000000000000000000000000:
        schedule.cancel_job(schedule)









