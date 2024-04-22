#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:06:07 2024

@author: leesnotebook
"""
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

btc_amount = 10.8714
eth_amount = 28.4544
usdt_amount = 444651
cash_amount = 365000000
dunamu_amount = 350000000

nest_asyncio.apply()





btc_price = pybithumb.get_current_price("BTC")
eth_price = pybithumb.get_current_price("ETH")
usdt_price = pybithumb.get_current_price("USDT")
valor_price = pybithumb.get_current_price("VALOR")
balance = round((btc_amount*btc_price)+(eth_amount*eth_price)+(usdt_amount*usdt_price),2) + \
        cash_amount + dunamu_amount
balance = format(  round(balance,0)  , ',')

message_balance = "💰보유량 \n ✅BTC:" + str(btc_amount) + "개 ="+str(format(round(btc_amount*btc_price,0),',')) +"원  \n ✅USDT:"\
    + str(usdt_amount) + "개 ="+str(format(round(usdt_amount*usdt_price,0),',')) +"원 \n ✅ETH:"\
    + str(eth_amount) + "개 ="+str(format(round(eth_amount*eth_price,0),',')) +"원\n ✅현금:"+str(format(cash_amount,','))+"원 \n ✅두나무:"+str(format(dunamu_amount,','))+\
        "원  \n 💲총 현금성 자산:" + str(balance)+"원 \n\n" + " 📃회수할자금\n" + \
            " 1️⃣.이게임,머니스왑,누리풋볼(최재혁계정환수) 쿠코인 디파짓 \n 2️⃣.오상훈,임지윤,MAX대여금 \n 3️⃣.밸러정산 \n 4️⃣.김진우,김철수\n"\
              +" 5️⃣.애니멀고 광복회, 주형"

message_will = "키타, 무다이 대기중"
message_lee = message_balance + "\n\n 🆕코인들시세 \n" 

async def main1(chat_id, token, message): #자산 알림봇

    
    bot = telegram.Bot(token = token)
    await bot.send_message(chat_id, message )

#📢📣☑️⬆️⬇️💲🔤📈📉💸⌛️🔈🆕📣🔥💥
#1️⃣2️⃣3️⃣4️⃣5️⃣⛳️🌟👍🙏▶️😈🐻🌎💻🖥⏱⏰✉️📕📊📃🗓🔒🖊❗️6️⃣7️⃣8️⃣9️⃣🔟🔺⬆️⬇️
#    1️⃣.  2️⃣.  3️⃣.  4️⃣.  5️⃣.  6️⃣.  7️⃣.  8️⃣.  9️⃣. 🔟






key = "2a2aa6a3253f54b7569fdc275f09c2f6"
secret = "fcb41b3afe326eee355e4e0e2dd3f73dba2f6975c3ba130c5b9462e632b97a29"
get = getinfo.get_crypto_info(key, secret)
gate_gomd = get.gateioex("GOMD")
gate_trcl = get.gateioex("TRCL")
bitget_gomd = get.bitgetex("GOMD")
gate_ad = get.gateioex("AD")
gate_egame = get.gateioex("EGAME")
gate_nrfb = get.gateioex("NRFB")
gate_mswap = get.gateioex(("MSWAP"))
gate_cup = get.gateioex("CUP")
gate_toms = get.gateioex("TOMS")


message_lee = message_lee + "\n📣"+gate_ad +"\n📣"+gate_egame + "\n📣"+gate_gomd + "\n📣"+gate_trcl + \
    "\n📣"+gate_nrfb + "\n📣"+gate_mswap + "\n📣"+gate_toms + "\n📣<BITHUMB-VALOR시세"+str(valor_price)+"원\n"+ \
        "📣<BITHUMB-BTC시세"+str(format(btc_price,','))+"원"

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
    
    
message_chikyu = "🆕"+ gate_ad + "\n🆕"+ gate_egame + "\n    🔥잔고현황\n📣" + "STO와 계정 준비중" +\
                    "\n\n  📈정산현황 : 업데이트 예정"




#자산 알림 

asyncio.run(main1(chat_id_leeb,token_lee,message_lee )) #Brown에게 재산전송
asyncio.run(main1(chat_id_ray,token_lee,message_lee ))  #Rayburg에게 재산전송


#코인 시세알림 

#윌
asyncio.run(main1(chat_id_will, token_will, message_will)) #윌 봇  
asyncio.run(main1(chat_id_leeb, token_will, message_will)) #윌 봇
asyncio.run(main1(chat_id_ray, token_will, message_will)) #윌 봇

#장
asyncio.run(main1(chat_id_jang, token_jang, message_jang))
asyncio.run(main1(chat_id_leeb, token_jang, message_jang))
asyncio.run(main1(chat_id_ray, token_jang, message_jang))
#치규
asyncio.run(main1(chat_id_chikyu, token_chikyu, message_chikyu))
asyncio.run(main1(chat_id_leeb, token_chikyu, message_chikyu))
asyncio.run(main1(chat_id_ray, token_chikyu, message_chikyu))












