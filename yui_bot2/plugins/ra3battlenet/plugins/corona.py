from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment
import requests

corona = on_fullmatch(["战网日冕数据"])


@corona.handle()
async def _():
    url = "http://api.ra3battle.cn/api/server/status"
    resq = requests.get(url)
    if len(resq.json()["players"]) >= 1:
        arr_games = len(resq.json()["games"])  # 对局总数
        automatch = len(resq.json()["automatch"])
        print("日冕数据")
        x = 0
        y = 0
        m = 0
        n = 0
        b = 0

        while x < arr_games:
            if resq.json()["games"][x]["mod"] == 'corona':
                if resq.json()["games"][x]["gamemode"] == 'closedplaying':
                    m = m + 1
                if resq.json()["games"][x]["gamemode"] == 'openstaging':
                    n = n + 1
            x = x + 1
        while y < automatch:
            if resq.json()["automatch"][y]["mod"] == 'corona3192':
                b = b + 1
            y = y + 1
        await  corona.finish(MessageSegment.text(
            "------------------------------" + "\n" + "日冕正在进行游戏的房间数：" + str(
                m) + "\n" + "日冕正在准备的房间数：" + str(n) + "\n" + "正在进行日冕匹配对战的房间：" + str(
                b) + "\n" + "------------------------------"))
    else:
        await  corona.finish(MessageSegment.text("获取数据为空，请稍后再试"))
