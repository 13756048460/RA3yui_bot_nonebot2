from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import Message
from nonebot.permission import SUPERUSER

sldw = on_fullmatch({"苏联单位价格"})
ma = on_fullmatch({"价格查询列表"})
xl = on_fullmatch({"血量查询列表"})
sljz = on_fullmatch({"苏联建筑价格"})
mjdw = on_fullmatch({"盟军单位价格"})
mjjz = on_fullmatch({"盟军建筑价格"})
sydw = on_fullmatch({"升阳/帝国单位价格", "升阳单位价格", "帝国单位价格"})
syjz = on_fullmatch({"升阳/帝国建筑价格", "升阳建筑价格", "帝国建筑价格"})

@xl.handle()
async def _():
     await xl.finish(Message("-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-----------------------"+"\n"+"苏联建筑血量"+"\n"+"苏联单位血量"+"\n"+"-----------------------"+"\n"+"盟军建筑血量"+"\n"+"盟军单位血量"+"\n"+"-----------------------"+"\n"+"升阳/帝国建筑血量"+"\n"+"升阳/帝国单位血量"+"\n"+"-----------------------"))

@ma.handle()
async def _():
    await ma.finish(Message(
        "-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------" + "\n" + "苏联建筑价格" + "\n" + "苏联单位价格" + "\n" + "-----------------------" + "\n" + "盟军建筑价格" + "\n" + "盟军单位价格" + "\n" + "-----------------------" + "\n" + "升阳/帝国建筑价格" + "\n" + "升阳/帝国单位价格" + "\n" + "-----------------------"))


@sldw.handle()
async def _():
    await sldw.finish(Message(
        "-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------" + "\n" + "战熊：225$" + "\n" + "动员兵：100$" + "\n" + "防空步兵：400$" + "\n" + "战斗工兵：500$" + "\n" + "磁暴部队：750$" + "\n" + "娜塔莎：2000$" + "\n" + "苏联矿车：1400$" + "\n" + "史普尼克勘探车：1200$" + "\n" + "恐怖机器人：600$" + "\n" + "镰刀机甲：900$" + "\n" + "牛蛙：900$" + "\n" + "铁锤坦克：1000$" + "\n" + "磁暴坦克：2200$" + "\n" + " V4导弹发射车：1200$" + "\n" + "天启坦克：2000$" + "\n" + "双刃直升机：1200$" + "\n" + "米格战斗机：1000$" + "\n" + "基洛夫飞艇：2500$" + "\n" + "磁暴快艇：1000$" + "\n" + "阿库拉潜艇：1800$" + "\n" + "无畏战列舰：2000$" + "\n" + "苏联基地车：5000$" + "\n" + "-----------------------"))


@sljz.handle()
async def _():
    await sljz.finish(Message(
        "-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------" + "\n" + "苏联建造场：5000$" + "\n" + "反应堆：800$" + "\n" + "军营：500$" + "\n" + "苏联矿石精炼厂：2000$" + "\n" + "战争工厂：2000$" + "\n" + "海军造船厂：1000$" + "\n" + "机场：1000$" + "\n" + "超级反应堆：2000$" + "\n" + "作战实验室：3000$" + "\n" + "压碎起重机：1500$" + "\n" + "苏联围墙：10$" + "\n" + "哨兵枪：800$" + "\n" + "防空炮：800$" + "\n" + "磁暴线圈：1500$" + "\n" + "铁幕装置：1500$" + "\n" + "真空内爆弹：2500$" + "\n" + "-----------------------"))


@mjjz.handle()
async def _():
    await mjjz.finish(Message(
        "-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------" + "\n" + "盟军建造场：5000$" + "\n" + "发电厂：800$" + "\n" + "新兵训练营：500$" + "\n" + "盟军矿石精炼厂：2000$" + "\n" + "装甲工厂：2000$" + "\n" + "海港：1000$" + "\n" + "空军基地：1000$" + "\n" + "科技中心：1500$" + "\n" + "盟军围墙：10$" + "\n" + "多功能炮塔：800$" + "\n" + "光谱塔：1200$" + "\n" + "超时空传送：1500$" + "\n" + "质子撞击炮：2500$" + "\n" + "-----------------------"))


@mjdw.handle()
async def _():
    await mjdw.finish(Message(
        "-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------" + "\n" + "警犬：200$" + "\n" + "维和步兵：200$" + "\n" + "标枪兵：300$" + "\n" + "工程师：500$" + "\n" + "间谍：1000$" + "\n" + "谭雅：2000$" + "\n" + "勘探者：1000$" + "\n" + "激流ACV：750$" + "\n" + "多功能步兵车：800$" + "\n" + "守护者坦克：950$" + "\n" + "雅典娜炮：1400$" + "\n" + "幻影坦克：1600$" + "\n" + "海豚：750$" + "\n" + " 水翼船：900$" + "\n" + "突袭驱逐舰：1500$" + "\n" + "航空母舰：2000$" + "\n" + "维和轰炸机：1200$" + "\n" + "阿波罗战斗机：1000$" + "\n" + "冰冻直升机：1600$" + "\n" + "世纪轰炸机：2000$" + "\n" + "盟军基地车：5000$" + "\n" + "-----------------------"))


@sydw.handle()
async def _():
    await sydw.finish(Message(
        "-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------" + "\n" + "爆裂机器人：300$" + "\n" + "帝国武士：150$" + "\n" + "坦克杀手：300$" + "\n" + "工兵：500$" + "\n" + "忍者：1000$" + "\n" + "火箭天使：900$" + "\n" + "欧米茄百合子：2000$" + "\n" + "帝国矿车：1400$" + "\n" + "迅雷运输艇：500$" + "\n" + "天狗机甲：800$" + "\n" + "打击者-VX：1200$" + "\n" + "海啸坦克：1000$" + "\n" + "鬼王：2000$" + "\n" + "波能坦克：1800$" + "\n" + "长枪迷你潜艇：800$" + "\n" + "海翼：1100$" + "\n" + "薙刀巡洋舰：1800$" + "\n" + "将军战列舰：2200$" + "\n" + "帝国基地车：5000$" + "\n" + "-----------------------"))


@syjz.handle()
async def _():
    await syjz.finish(Message(
        "-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------" + "\n" + "帝国建造场：5000$" + "\n" + "瞬息发电厂：800$" + "\n" + "瞬息道场：500$" + "\n" + "帝国矿石精炼厂：2500$" + "\n" + "机甲工厂：2000$" + "\n" + "帝国码头：1000$" + "\n" + "纳米主机：2500$" + "\n" + "帝国围墙：10$" + "\n" + "防卫者—VX：800$" + "\n" + "波能塔：1400$" + "\n" + "纳米虫群：1500$" + "\n" + "超能波毁灭：2500$" + "\n" + "-----------------------"))
