from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, Message
import requests

ph = on_fullmatch("战网日冕天梯排行")
@ph.handle()
async def _():
    data = []
    s = requests.get("https://api.ra3battle.cn/api/stats/season/current/result")
    url = "https://api.ra3battle.cn/api/stats/ladder/corona/1v1/records/page/1/result"
    resq = requests.get(url)
    peapo = len(resq.json()["records"])
    a = 0
    if peapo < 10:
        names = str(resq.json()["records"][0]["personaName"])
        rank = str(resq.json()["records"][0]["rank"])
        elo = str(resq.json()["records"][0]["elo"])
        primaryFaction = str(resq.json()["records"][0]["primaryFaction"])
        if primaryFaction == "Empire":
            primaryFaction = "帝国"
        if primaryFaction == "Allied":
            primaryFaction = "盟军"
        if primaryFaction == "Soviet":
            primaryFaction = "苏联"
        if primaryFaction == "Celestial":
            primaryFaction = "神州"
        out = rank + "  " + names + "  " + elo + "  " + primaryFaction + "\n" + "因不足10名，懒得做了，所以只展示第一名"
        data.append(out)
    else:
        while a <= 9:
            names = str(resq.json()["records"][a]["personaName"])
            rank = str(resq.json()["records"][a]["rank"])
            elo = str(resq.json()["records"][a]["elo"])
            primaryFaction = str(resq.json()["records"][a]["primaryFaction"])
            if primaryFaction == "Empire":
                primaryFaction = "帝国"
            if primaryFaction == "Allied":
                primaryFaction = "盟军"
            if primaryFaction == "Soviet":
                primaryFaction = "苏联"
            if primaryFaction == "Celestial":
                primaryFaction = "神州"
            out = rank + "  " + names + "  " + elo + "  " + primaryFaction+"\n"
            a = a + 1
            data.append(out)
    output = ''.join(data)
    await  ph.finish(Message("----------------------------\n战网日冕1v1天梯前十 \n赛季："+s.json()["chineseName"]+"\n----------------------------\n排行  马甲名  ELO  主要国家\n----------------------------\n"+output+"\n----------------------------"))




