from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import Message

world = on_fullmatch({"b站列表"})
fl = on_fullmatch({"飞龙b站"})
kunagisa = on_fullmatch({"玖渚智心b站"})
tfq = on_fullmatch({"塔防群b站"})
tfqzb = on_fullmatch({"塔防b站直播链接"})
xm = on_fullmatch({"小梦b站"})
ss = on_fullmatch({"时殇b站"})
mz = on_fullmatch({"沐泽b站"})
mcpdb = on_fullmatch({"mcpdb站"})
gez = on_fullmatch({"塔防鸽子b站"})
dsge = on_fullmatch({"大爽歌b站"})
swg = on_fullmatch({"苏维鸽b站"})
jaq = on_fullmatch({"假爱情b站"})


@world.handle()
async def _():
    await world.finish(Message(
        "-------------------------" + "\n" + "龙飞b站" + "\n" + "玖渚智心b站" + "\n" + "塔防群b站" + "\n" + "塔防b站直播链接" + "\n" + "小梦b站" + "\n" + "时殇b站" + "\n" + "沐泽b站" + "\n" + "mcpdb站" + "\n" + "塔防鸽子b站" + "\n" + "大爽歌b站" + "\n" + "苏维鸽b站" + "\n" + "假爱情b站" + "\n" + "-------------------------"))


@fl.handle()
async def _():
    await fl.finish(Message("https://space.bilibili.com/349126866"))

@kunagisa.handle()
async def _():
    await kunagisa.finish(Message("https://space.bilibili.com/106111618"))

@tfq.handle()
async def _():
    await tfq.finish(Message("https://space.bilibili.com/478585756"))

@tfqzb.handle()
async def _():
    await tfqzb.finish(Message("https://live.bilibili.com/21662753"))

@xm.handle()
async def _():
    await xm.finish(Message("空间https://space.bilibili.com/292328949\n直播间https://live.bilibili.com/22709259?visit_id=qyta6ac31o0"))


@ss.handle()
async def _():
    await ss.finish(Message("个人空间：https://space.bilibili.com/39441173/\n直播链接：https://live.bilibili.com/4358337"))


@mz.handle()
async def _():
    await mz.finish(Message("https://live.bilibili.com/13399683"))


@mcpdb.handle()
async def _():
    await mcpdb.finish(Message("个人空间：https://space.bilibili.com/124026040/"))


@gez.handle()
async def _():
    await gez.finish(Message("个人空间：https://space.bilibili.com/51769177\n直播：https://live.bilibili.com/6034220"))


@dsge.handle()
async def _():
    await dsge.finish(Message("个人空间：https://space.bilibili.com/149259132/\n直播链接：https://live.bilibili.com/13337214"))


@swg.handle()
async def _():
    await swg.finish(Message("个人空间：https://space.bilibili.com/302062917/\n直播链接：https://live.bilibili.com/12986677"))


@jaq.handle()
async def _():
    await jaq.finish(Message("个人空间：https://space.bilibili.com/243291953/\n直播链接：https://live.bilibili.com/22699189"))



