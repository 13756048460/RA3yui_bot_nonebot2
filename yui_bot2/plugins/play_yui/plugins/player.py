from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment
import random

player = on_fullmatch("来根冰棍")


@player.handle()
async def _():
    text = ["大脚板", "绿舌头", "三色杯", "夏威夷雪糕", "大布丁", "小布丁", "奶砖", "老冰棍", "碎冰冰",
            "雪莲", "雪乐冰", "兵工厂夏威夷果", "冰工厂山楂棒冰", "玉米香", "椰子灰", "巧乐兹", "托肥",
            "奶提子", "糯米糍", "八喜", "梦龙", "麦酷狮", "红枣牛奶棒冰", "哈根达斯冰淇淋", "旺旺吸吸冰"]
    text_t = ["这是给你的冰棍哦，小心吃多了坏肚子","来跟冰棍吧，小心别化掉哦","吃冰棍吗，给你的"]
    await player.finish(random.choice(text_t)+MessageSegment.text("\n")+MessageSegment.text("获得了冰棍：（“")+random.choice(text)+MessageSegment.text("”）"))