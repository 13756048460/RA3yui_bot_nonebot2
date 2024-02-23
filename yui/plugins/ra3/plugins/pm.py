from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment
import requests

zw = on_fullmatch("战网阵营胜率")
@zw.handle()
async def _():
    qb = requests.get("https://api.ra3battle.cn/api/stats/1v1/factions/ra3/0")
    a_Alliedwins = qb.json()["Allied"]["wins"]
    a_Alliedtotal = qb.json()["Allied"]["total"]
    a_Sovietwins = qb.json()["Soviet"]["wins"]
    a_Soviettotal = qb.json()["Soviet"]["total"]
    a_Empirewins = qb.json()["Empire"]["wins"]
    a_Empiretotal = qb.json()["Empire"]["total"]
    syl = a_Empiretotal + a_Soviettotal + a_Alliedtotal

    bb = requests.get("https://api.ra3battle.cn/api/stats/1v1/factions/ra3/3")
    b_Alliedwins = bb.json()["Allied"]["wins"]
    b_Alliedtotal = bb.json()["Allied"]["total"]
    b_Sovietwins = bb.json()["Soviet"]["wins"]
    b_Soviettotal = bb.json()["Soviet"]["total"]
    b_Empirewins = bb.json()["Empire"]["wins"]
    b_Empiretotal = bb.json()["Empire"]["total"]
    syl_b = b_Empiretotal + b_Soviettotal + b_Alliedtotal


    await zw.finish(MessageSegment.text("----------------------------\n阵营胜率全部排名\n----------------------------\n阵营  胜率 使用率 胜场 场次\n----------------------------\n"+"盟军  "+'{:.1f}%'.format(a_Alliedwins/a_Alliedtotal*100)+"  "+'{:.1f}%'.format(a_Alliedtotal/syl*100)+"  "+str(a_Alliedwins)+"  "+str(a_Alliedtotal)+"\n"+"苏联  "+'{:.1f}%'.format(a_Sovietwins/a_Soviettotal*100)+"  "+'{:.1f}%'.format(a_Soviettotal/syl*100)+"  "+str(a_Sovietwins)+"  "+str(a_Soviettotal)+"\n升阳  "+'{:.1f}%'.format(a_Empirewins/a_Empiretotal*100)+"  "+'{:.1f}%'.format(a_Empiretotal/syl*100)+"  "+str(a_Empirewins)+"  "+str(a_Empiretotal)
                                        +"\n----------------------------\n阵营胜率1200排名\n----------------------------\n阵营  胜率 使用率 胜场 场次\n----------------------------\n"+"盟军  "+'{:.1f}%'.format(b_Alliedwins/b_Alliedtotal*100)+"  "+'{:.1f}%'.format(b_Alliedtotal/syl_b*100)+"  "+str(b_Alliedwins)+"  "+str(b_Alliedtotal)+"\n"+"苏联  "+'{:.1f}%'.format(b_Sovietwins/b_Soviettotal*100)+"  "+'{:.1f}%'.format(b_Soviettotal/syl_b*100)+"  "+str(b_Sovietwins)+"  "+str(b_Soviettotal)+"\n升阳  "+'{:.1f}%'.format(b_Empirewins/b_Empiretotal*100)+"  "+'{:.1f}%'.format(b_Empiretotal/syl_b*100)+"  "+str(b_Empirewins)+"  "+str(b_Empiretotal)+
                                        "\n----------------------------"))