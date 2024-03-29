from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import Message , MessageSegment
import random

jzsjcx = on_fullmatch("建造时间查询列表")
suljzsj = on_fullmatch("苏联建筑建造时间")
sldw = on_fullmatch("苏联单位建造时间")
mjjz = on_fullmatch("盟军建筑建造时间")
mjdw = on_fullmatch("盟军单位建造时间")
dgjz = on_fullmatch({"升阳/帝国建造时间", "升阳单位建造时间", "帝国单位建造时间"})
dgdw = on_fullmatch({"升阳/帝国建造时间", "升阳单位建造时间", "帝国单位建造时间"})

@jzsjcx.handle()
async def _():
    await jzsjcx.finish(Message("-----------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-----------------------\n苏联建筑建造时间\n苏联单位建造时间\n-----------------------\n盟军建筑建造时间\n盟军单位建造时间\n-----------------------\n升阳/帝国建筑建造时间\n升阳/帝国单位建造时间\n-----------------------"))

@suljzsj.handle()
async def _():
    await suljzsj.finish(Message(
        "-----------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-----------------------\n反应堆：0:10\n军营：0:10\n苏联矿石精炼厂：0:20\n战争工厂：0:20\n海军造船厂：0:20\n机场：0:30\n超级反应堆：0:30\n作战实验室：0:30\n压碎起重机：0:20\n苏联围墙：0:05\n哨兵枪：0:20\n防空炮：0:20\n磁暴线圈：0:30\n铁幕装置：0:30\n真空内爆弹：0:30\n-----------------------"))

@sldw.handle()
async def _():
    await sldw.finish(Message("-----------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-----------------------\n战熊：0:02\n动员兵：0:04\n防空步兵：0:05\n战斗工兵：0:10\n磁暴部队：0:10\n娜塔莎：0:30\n苏联矿车：0:20\n史普尼克勘探车：0:20\n恐怖机器人：0:05\n镰刀机甲：0:10\n牛蛙：0:10\n铁锤坦克：0:10\n磁暴坦克：0:22\nV4导弹发射车：0:15\n天启坦克：0:20\n双刃直升机：0:15\n米格战斗机：0:10\n基洛夫飞艇：0:30\n磁暴快艇：0:10\n阿库拉潜艇：0:20\n无畏战列舰：0:30\n苏联基地车：1:00\n-----------------------"))

@mjjz.handle()
async def _():
    await mjjz.finish(Message(
        "-----------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-----------------------\n发电厂：0:10\n新兵训练营：0:10\n盟军矿石精炼厂：0:20\n装甲工厂：0:20\n海港：0:20\n空军基地：0:15\n科技中心：0:30\n盟军围墙：0:05\n多功能炮塔：0:20\n光谱塔：0:20\n超时空传送：0:30\n质子撞击炮：0:30\n-----------------------"))

@mjdw.handle()
async def _():
    await mjdw.finish(Message("-----------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-----------------------\n警犬：0:02\n维和步兵：0:05\n标枪兵：0:05\n工程师：0:10\n间谍：0:10\n谭雅：0:30\n勘探者：0:20\n激流ACV：0:10\n多功能步兵车：0:10\n守护者坦克：0:10\n雅典娜炮：0:20\n幻影坦克：0:15\n海豚：0:10\n水翼船：0:10\n突袭驱逐舰：0:20\n航空母舰：0:30\n维和轰炸机：0:15\n阿波罗战斗机：0:10\n冰冻直升机：0:15\n世纪轰炸机：0:20\n盟军基地车：1:00\n-----------------------"))

@dgjz.handle()
async def _():
    await dgjz.finish(Message(
        "-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------\n瞬息发电厂：0:04/0:06\n瞬息道场：0:04/0:04\n帝国矿石精炼厂：0:04/0:16\n机甲工厂：0:04/0:12\n帝国码头：0:04/0:14\n纳米主机：0:04/0:26\n帝国围墙：0:05\n防卫者—VX：0:04/0:11\n波能塔：0:04/0:36\n纳米虫群：0:04/0:22\n超能波毁灭：0:04/0:22\n-----------------------"))

@dgdw.handle()
async def _():
    await dgdw.finish(Message("-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------\n爆裂机器人：0:05\n帝国武士：0:05\n坦克杀手：0:05\n工兵：0:10\n忍者：0:10\n火箭天使：0:10\n欧米茄百合子：0:30\n帝国矿车：0:20\n迅雷运输艇：0:05\n天狗机甲：0:10\n打击者-VX：0:10\n海啸坦克：0:10\n鬼王：0:20\n波能坦克：0:15\n长枪迷你潜艇：0:10\n海翼：0:10\n薙刀巡洋舰：0:18\n将军战列舰：0:22\n帝国基地车：1:00\n-----------------------"))
