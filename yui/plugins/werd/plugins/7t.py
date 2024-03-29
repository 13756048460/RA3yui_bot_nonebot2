from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import Message , MessageSegment


gfqt = on_fullmatch("官方七图")
zdys = on_fullmatch("战斗要塞简介")
kbn = on_fullmatch("卡巴纳共和国简介")
hsd = on_fullmatch("火山岛简介")
gyq = on_fullmatch("工业区简介")
wxd = on_fullmatch("无限岛简介")
xl = on_fullmatch("雪梨简介")
sm = on_fullmatch("神庙简介")


@gfqt.handle()
async def _():
    a = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n------------------------------\n战斗要塞简介\n卡巴纳共和国简介\n火山岛简介\n工业区简介\n无限岛简介\n雪梨简介\n神庙简介\n------------------------------"
    await gfqt.finish(a)


@zdys.handle()
async def _():
    a = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n------------------------------\n" + MessageSegment.image(
        "C:/Users/Administrator/Desktop/新建文件夹/yui_bot/bkimg/zhand.jpg") + "\n战斗要塞Battlebase Beta：\n海上两个矿，要塞上有8个矿，地图分两层，有监视站和油井，众多房子。\n\n这是一座来自于帝国的浮岛战斗要塞，看上去整座要塞空无一人，或许是帝国早已经将此地遗弃，而两位指挥官将在这座要塞上展开战斗，整张地图为对称设计，非常适合进行竞技性比赛，地图为中型地图，共分两大块区域，分别是海洋和要塞，而要塞又分上下两层，整座要塞拥有较多的房子，指挥官可以通过占领房子来进行防守和进攻并在有些时候能够让你控制一些关键节点，同时地图上的监视站和中立油井可以让指挥官的优势进一步扩大，矿区位置大多处在要塞上，显然大部分的战斗将会在要塞上进行，不过海洋中的矿产或许在某些时刻会对战局产生奇特的效果。指挥官，欢迎来到战斗要塞！\n------------------------------"
    await zdys.finish(a)


@kbn.handle()
async def _():
    a = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n------------------------------\n" + MessageSegment.image(
        "C:/Users/Administrator/Desktop/新建文件夹/yui_bot/bkimg/kbn.jpg") + "\n卡巴纳共和国 CabanaRepublic ：\n海上四个矿，陆地6个矿，左右对称，中心有大量房子，有两处高地，有油井监视站和医院，零星分布众多房子\n\n欢迎来到卡巴纳共和国，这座岛屿国度今天就会迎来两位新的客人，而当中只能有一位能够安心的享受卡巴纳共和国的美丽景色，当然，只要这两位不会把岛屿破坏的太严重。整张地图为对称设计，非常适合竞技性比赛，地图为中型地图，周围环绕的海洋以及丰富的海矿资源意味着海军可以发挥更大的作用。同时，卡巴纳共和国的居民房屋可以让士兵进行驻扎以此来保护你的矿场，或者控制一些关键节点，不要忘记了岛上的中立油田和监视站以及医院，如果能够占领它们或许你可以从你的对手那取得较大的优势，注意那些小山丘，你肯定不想有什么东西突然从阴影中突然出现。看上去今天的卡巴纳共和国非常不太平，指挥官。\n------------------------------"
    await kbn.finish(a)


@hsd.handle()
async def _():
    a = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n------------------------------\n" + MessageSegment.image(
        "C:/Users/Administrator/Desktop/新建文件夹/yui_bot/bkimg/hsd.jpg") + "\n火山岛 Fire Island：\n海上两个矿，陆地8个矿，中间有两堵高山，有监视站和油井，没有房子\n\n这座处在太平洋上的火山岛今天下起了蒙蒙细雨，而岛上的复活节雕像似乎在等待两位刚刚踏足这块岛的指挥官决出最终的胜负，准备向后来者诉说胜利者的故事。整张地图为对称设计，非常适合竞技性比赛，地图为小型地图，意味着快速进攻将是一个非常好的战术，但是地图中的两个巨大山脉将地图分为三个部分，这也可以让一些快速迂回的骚扰柔性战法得以大展拳脚，由于这块岛屿没有中立的房子，驻扎士兵控制节点的方法将无法进行，不过地图上的油井和监视站依旧可以在你使用这些战术的时候提供巨大的便利，是使用如火一般的快速进攻战术快速击败敌人，还是使用柔性似水的快速迂回骚扰牵制对方，我想在火山岛的这个夜晚注定不眠，指挥官。\n------------------------------"
    await hsd.finish(a)


@gyq.handle()
async def _():
    a = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n------------------------------\n" + MessageSegment.image(
        "C:/Users/Administrator/Desktop/新建文件夹/yui_bot/bkimg/gyq.jpg") + "\n工业区 Industrial Strength：\n海上4个矿，陆地6个矿。出生点位被高地包围，有监视站和油井和车库，有众多房子。\n\n 工业是一种非常强大的力量，它可以给人民带来福祉，但也可以带来战争。谁拥有了工业力量，谁就能征服世界。现在，有两位指挥官将会在这片工业区展开一场激烈的战斗。整张地图为对称设计，非常适合竞技性比赛，本地图为中型地图，周围环绕的海洋可以让你尝试使用海军取得胜利。指挥官的出生地被一圈高地所包围，总共有两个出入口，因此，正面突进高地内的矿区将会变得异常困难，不过，随时注意高地上的情况，因为敌人可能会采取高打低的方式进攻你的矿区，地图上有着许多工业区厂房，占领它们可以让你有效的限制对方的行动，同时占领地图上的油井和监视站可以为你取得大量的战术优势，注意地图中心的车库，占领他可以让你的工业战车能够所向披靡。指挥官，该使用你的工业力量击败敌人了！\n------------------------------"
    await gyq.finish(a)


@wxd.handle()
async def _():
    a = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n------------------------------\n" + MessageSegment.image(
        "C:/Users/Administrator/Desktop/新建文件夹/yui_bot/bkimg/wxd.jpg") + "\n无限岛 infinity isle ：\n海上四个矿，分布在海洋和悬崖下，陆地6矿，中心有一条道以及一所监视站，靠近玩家位置有房子和油井\n\n是谁发现了这块岛屿并命名它为无限岛，已经无法考证。不过有一个说法是这个岛屿的形状形似无限符号，不过这并不妨碍两位指挥官在这块岛上所进行的战斗。整张地图为对称设计，非常适合竞技性比赛，地图为小型地图，整张地图非常简单，只有一条路口可以让你的陆地军队进攻对方基地，因此正面战场将会非常激烈，不过岛屿周围被大片的海洋环绕，可以让你的海军和机动部队直接扰过敌方正面进攻其软肋，不要忘记了地图上的油井，它可以为你提供源源不断地资金，注意地图中心的监视站，占领他可以让你对敌方的情况了如指掌。无限岛上无限的战斗，带来的是无限的胜利，还是无限的失败，让我们拭目以待。\n------------------------------"
    await wxd.finish(a)


@xl.handle()
async def _():
    a = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n------------------------------\n" + MessageSegment.image(
        "C:/Users/Administrator/Desktop/新建文件夹/yui_bot/bkimg/xl.jpg") + "\n雪梨 Snow Plow ：\n海上4个矿，陆地6个矿，中心有大路，两边有桥梁，有监视站和油井，有众多房子。\n\n这座处于寒冷地区的岛屿常年被积雪覆盖，由于寒冷，只有零星的平民住在这里，不过接下来两位指挥官在这里发生的战斗很可能会让此地区的温度升温。整张地图为对称设计，非常适合竞技性比赛，地图为小型地图，分为上下两部分，中间的一条河流被大路一分为二，两边的有桥梁进行连接，由于周围海域的矿区并不丰富，因此战斗将会围绕中心大路和河流展开，指挥官可以选择通过中心大陆直接向对方发动攻击，也可以选择通过两边桥梁发动奇袭，不过需要注意的是桥梁非常脆弱，你可不想让你的部队去感受冰冷的海水。同时，岛上的居民房子可以通过驻守来进行防御矿区或进攻，随时留意地图上的油井和监视站，这或许可以让你得到些许优势。这里可能非常寒冷，但是这里的战斗将会非常焦灼。\n------------------------------"
    await xl.finish(a)


@sm.handle()
async def _():
    a = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n------------------------------\n" + MessageSegment.image(
        "C:/Users/Administrator/Desktop/新建文件夹/yui_bot/bkimg/sm.jpg") + "\n神庙：\n海上四个矿，陆地6个矿，中间有高地和神庙，有监视站和油井，有众多房子\n\n敬业的考古学家在这座岛上发现了新的文明遗迹，或许可以有助于我们了解古代文明的历史和发展，不过，看上去并不是只有你一个人对此地的考古发现感兴趣。整张地图为对称设计，非常适合竞技性比赛，地图为小型地图，周围被海洋包围，同时海上丰富的矿区可以让你选择下海进行发展，这意味着指挥官可以选择海上进攻，而陆地则分为三层，中间高地第一层拥有两个矿位，前进压迫攻势亦是一个不错的选择，同时，中心区域的神庙如果能够被驻军占领，那么可以为你的压迫攻势如虎添翼，注意岛上其他的中立建筑，油田和监视站，占领他们可以让你更有效的控制关键节点。尽量不要将此地的考古遗迹破坏的太严重了，指挥官。\n------------------------------"
    await sm.finish(a)
