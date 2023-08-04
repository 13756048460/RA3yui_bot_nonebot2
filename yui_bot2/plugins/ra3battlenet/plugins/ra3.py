from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment
import requests
import sys
ra3 = on_fullmatch(["战网数据"])


@ra3.handle()
async def _():
    ratxt='C:/Users/Administrator/Desktop/ra3data/ra3data.txt'
    url = "http://api.ra3battle.cn/api/server/status"
    resq = requests.get(url)

    if len(resq.json()["players"]) >= 1:
        palyer_data = len(resq.json()["players"])-1  # 玩家总数
        arr_games = len(resq.json()["games"])  # 对局总数
        file = open(ratxt)
        ra3data = file.read()
        file.close()
        if int(ra3data) > palyer_data:
            file.close()
        else:
            file = open(ratxt, 'w+', encoding='utf-8')
            file.write(str(palyer_data))
        file = open(ratxt)
        ra3data = file.read()
        print(ra3data)
        a = 0
        x = 0
        b = 0
        m = 0
        while x < arr_games:
            a = a + len(resq.json()["games"][x]["players"])
            x = x + 1
        while b <= arr_games:
            if resq.json()["games"][b - 1]["gamemode"] == 'closedplaying':
                m = m + 1
            b = b + 1
        await  ra3.finish(MessageSegment.text(
            "------------------------------"+"\n"+"峰值人数："+ra3data+"\n"+"当前在线人数：" + str(palyer_data) + "\n" + "正在对局玩家：" + str(a)+"\n"+"闲置玩家："+str(palyer_data-a)+"\n"+"------------------------------"+"\n"+"1v1自动匹配正在寻找对局的玩家为："+str(resq.json()["automatching"]["count1v1"])+"\n"+"人机对战正在寻找对局的玩家为："+str(resq.json()["automatching"]["countPve"])+"\n"+"执政官挑战正在寻找对局的玩家为："+str(resq.json()["automatching"]["countArchon"])+"\n"+"------------------------------"+"\n"+"正在进行匹配对战的房间总数："+str(len(resq.json()["automatch"]))+"\n"+"正在进行游戏的房间个数："+str(m)+"\n"+"正在准备的房间个数："+str(arr_games-m+1)+"\n"+"------------------------------"))
        file.close()
    else:
        await  ra3.finish(MessageSegment.text("获取数据为空，请稍后再试"))


