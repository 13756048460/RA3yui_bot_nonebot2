import json

from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, event, Bot, GroupMessageEvent
import requests

fj = ra3 = on_fullmatch({"正在准备房间","房间数据","正在准备的房间","查找房间"})
@fj.handle()
async def _(event: GroupMessageEvent, bot: Bot):
    with open("C:/Users/Administrator/Desktop/新建文件夹/yui_bot/zh.json", "r") as f:
        js = json.load(f)
    nameszh = js["Map"][0]
    nameszhar = js["Map"][1]
    nameszhars = js["Map"][2]
    data = []
    url = "https://api.ra3battle.cn/api/server/status"
    resq = requests.get(url)
    gamesNumber = len(resq.json()["games"])

    a = 0
    for i in range(gamesNumber):
        homeNames = resq.json()["games"][i]["hostname"]
        if resq.json()["games"][i]["gamemode"] == "openstaging":
            if not resq.json()["games"][i]["players"]:
                nameZero = "Null"
            else:
                nameZero = str(resq.json()["games"][i]["players"][0]["name"])
            home = homeNames.split()[1]
            mod = str(resq.json()["games"][i]["mod"])
            peapoNumber = len(resq.json()["games"][i]["players"])
            if mod == "RA3":
                mod = "原版"
            if mod == "corona":
                mod = "日冕"
            mapName = str(resq.json()["games"][i]["mapname"])
            mapNameSTR = mapName.replace('\\', "/")
            lt = mapNameSTR.split("/")
            last = lt.pop()
            over = last.split(".")
            lsover = over[0]
            tlover = lsover.upper()
            if tlover in nameszh:
                lsover = nameszh.get(tlover)
            if tlover in nameszhar:
                lsover = nameszhar.get(tlover)
            if tlover in nameszhars:
                lsover = nameszhars.get(tlover)
            a += 1
            DeMap = " "
            urlm = "https://ra3.z31.xyz/v1/maps/?p=1&s=24&search=" + lsover
            mapsD = requests.get(urlm)
            Mapname = mapsD.json()
            if Mapname["count"] == 0:
                DeMap = "Null"
            else:
                file = Mapname["results"][0]["zip_file"]
                DeMap = file
            # data.append(
            #     "房间名：" + home + "\n" + "地图名：" + lsover + "\n" + "房主名：" + nameZero + "\n" + "MOD名：" + mod + "\n" + "房间内人数：" + str(
            #         peapoNumber) + "\n" +"地图下载链接："+"\n"+DeMap +"\n"+"------------------------------"+"\n")
            data.append(
                "房间名：" + home + "\n" + "地图名：" + lsover + "\n" + "房主名：" + nameZero + "\n" + "MOD名：" + mod + "\n" + "房间内人数：" + str(
                    peapoNumber) +"\n"+"------------------------------"+"\n")
    out = ''.join(data)
    textT = "正在准备的房间数：" + str(a) + "\n" + "------------------------------" + "\n"
    message = textT + out
        #await bot.send_group_forward_msg(
        #    group_id=event.group_id,
        #    messages=[
        #        {
        #            "type": "node",
        #            "data": {
        #                "name": "Yui_bot",
        #                "uin": bot.self_id,
        #                "content": message,
        #            },
        #        }
        #    ],
        #)
    await  fj.finish(MessageSegment.text(message))