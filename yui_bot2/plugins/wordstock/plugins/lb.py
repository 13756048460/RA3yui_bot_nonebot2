from nonebot import  on_fullmatch
from nonebot.adapters.onebot.v11 import Message, MessageSegment

baike = on_fullmatch("百科列表")
szcx = on_fullmatch("查询列表") 
world = on_fullmatch("关键词列表")
zwsj = on_fullmatch("战网数据列表")
kksk = on_fullmatch("数值可查询图表")
hjkksk = on_fullmatch("护甲可查询图表")


@baike.handle()
async def _():
    await  baike.finish(Message("-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------" + "\n" + "查询列表"+"\n"+"官方七图"+"\n"+"最高机密协议"+"\n"+"护甲系统"+"\n"+"武器系统"+"\n" +"经验机制"+"\n"+"快捷键"+"\n"+"维修公式"+"\n"+"什么是速度"+"\n" +"什么是修正比"+"\n" +"什么是碾压等级"+"\n" +"什么是警戒半径"+"\n" +"什么是清雾半径"+"\n" +"什么是建造/训练时长"+"\n" +"什么是建筑维修"+"\n" +"什么是一轮开火时间"+"\n" +"什么是一轮输出伤害"+"\n" +"什么是DPS"+"\n" +"什么是溅射半径"+"\n" +"什么是溅射伤害"+"\n" +"什么是步兵压制"+"\n" +"什么是护甲类型"+"\n" +"什么是步兵进驻"+"\n" +"什么是单位升级后的数值变化"+"\n" +"什么是冷冻伤害"+"\n" +"什么是视野残留机制"+"\n" +"-------------------------"))

@world.handle()
async def _():
    await  world.finish(Message(
        "-------------------------" +"\n"+"人物志列表"+ "\n" + "红3地图分类" + "\n" + "怎么下载日冕" + "\n" + "战网官网" + "\n" + "mod安装教程" + "\n" + "游戏汉化教程" + "\n" + "怎么下载起义" + "\n" + "怎么下载红警三" + "\n" + "塔防语音链接" + "\n" + "地图下载工具" + "\n" + "战网数据列表" + "\n"  + "百科列表" + "\n" +  "mod列表" +  "\n" +  "红警3语音包" +"\n"+"dx修复工具"+"\n"+"-------------------------"))

@szcx.handle()
async def _():
    await szcx.finish(Message("-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------\n协议查询列表\n血量查询列表\n价格查询列表\n建造时间查询列表\n-------------------------\n数值可查询图表\n单位+基础数值\n护甲可查询图表\n单位+护甲类型\n-------------------------"))

@zwsj.handle()
async def _():
    await  zwsj.finish(Message("-------------------------\n战网数据\n战网日冕数据\n战网天梯排行\n战网日冕天梯排行\n战网阵营胜率\n-------------------------"))

@kksk.handle()
async def _():
    await  kksk.finish(MessageSegment.image("file:///C:/Users/Administrator/Desktop/dww/dataBase.png"))

@hjkksk.handle()
async def _():
    await  hjkksk.finish(MessageSegment.image("file:///C:/Users/Administrator/Desktop/dww/Ra3dataBasepl2.png"))