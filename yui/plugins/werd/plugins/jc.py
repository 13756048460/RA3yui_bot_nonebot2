from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import Message , MessageSegment

ra3up = on_fullmatch({"怎么下载红警三起义","怎么下载起义", "怎样下载起义时刻", "怎样下载起义", "怎么下载起义时刻"})
ra3 = on_fullmatch({"怎么下载红警三", "怎么下载红警3", "怎样下载红警3", "怎样下载红警三", "怎么下载ra3"})
mapd = on_fullmatch({"怎么安装地图", "地图安装教程", "地图下载工具", "地图下载器"})
game_What = on_fullmatch(
    {"红警三正版怎么弄", "怎么装mod", "游戏怎么安装", "怎么安装mod", "mod安装教程", "游戏汉化教程", "怎么汉化"})
RA3BattleNet = on_fullmatch(
    {"怎么联机", "怎么下载战网", "战网官网", "战网怎么联机", "联机现在用什么", "现在联机都用什么"})
cdkey = on_fullmatch({"怎么修改cdk", "怎么修改CDK"})
arc = on_fullmatch({"怎么安装日冕", "怎么下载日冕"})
taft = on_fullmatch("红3地图分类")
mod_Don = on_fullmatch({"mod列表","mod群聊"})
Voice = on_fullmatch("红警3语音包")
tool = on_fullmatch("dx修复工具")
netd = on_fullmatch("net下载链接")


@mod_Don.handle()
async def _():
    await mod_Don.finish(MessageSegment.text("-------------------------"+"\n"+"Insurrection:群453239661"+"\n"+"科学Mod 1.91最终版（2023.10.25）：www.bilibili.com/read/cv27257448"+"\n"+"最终协议:群953437366"+"\n"+"Armor Rush:群622692891"+"\n"+"沙雕警戒3:群948371257"+"\n"+"龙霸天下:群150559741 群213356762"+"\n"+"将军2:群296524582"+"\n"+"The New World:群299420109"+"\n"+"Remix:群787717922"+"\n"+"冲突世界:群577591891"+"\n"+"Psyonic Omega:群334579291"+"\n"+"Dawn黎明MOD:群499406325"+"\n"+"Eisenreich:群653952489"+"\n"+"ChaosFA:群165624222"+"\n"+"强权战争:群891321634 群684025988"+"\n"+"幻次元:群813567480 群1135458883"+"\n"+"宿敌:群837758987"+"\n"+"崩坏3:群832289938"+"\n"+"塔防大师:群915031091 群652469807"+"\n"+"FS+TCB:群689669808"+"\n"+"尤里归来:群1081649797"+"\n"+"二重进化:群1043277809"+"\n"+"TECH-SHUFFLE（科技重组MOD）:群249748868"+"\n"+"日冕Corona:群853481766"+"\n"+"德意志同盟中央歌剧院:群801141387"+"\n"+"战时联合:群781467431"+"\n"+"地狱行军:群675257891"+"\n"+"回春:群727525312"+"\n"+"Uprising Reborn:群701203945"+"\n"+"猫球警戒:群854509748"+"\n"+"RAC:群477375940"+"\n"+"-------------------------"))

@ra3.handle()
async def _():
    await ra3.finish(Message("命令与征服：红色警戒3原版加群：607024829 \n 命令与征服：红色警戒3阉割版.exe:http://mtw.so/5EFfiM \n下载站：http://files.ra3.cc/ra3\n此压缩包文件是由小琪打包完成的\n 红3bwiki网站：https://wiki.biligame.com/redalert3"))


@ra3up.handle()
async def _():
    await ra3up.finish(Message("命令与征服：红色警戒3起义时刻与起义时刻电影包加群：1098605891n\n下载站：http://files.ra3.cc/ra3"))


@mapd.handle()
async def _():
    await mapd.finish(Message( "红警3地图工具最新版3.76，Q群:953371430 \n使用教程：https://b23.tv/kvfOUUf \n下载链接：http://mtw.so/6vYFEC \n支持筛选地图下载，自制地图上传，本地地图管理，万能工具修复游戏问题，录像管理，地图页面可评论。 \n红警3地图百科:http://mtw.so/6ostdr，地编新版研究群：613550502"))


@RA3BattleNet.handle()
async def _():
    await RA3BattleNet.finish(Message(
        "战网正式版已于2023.3.23日晚上开始正式上线。战网官网：https://ra3battle.net \n战网图文教程链接：http://mtw.so/5MW4fg \n战网视频教程：http://mtw.so/6gWfww \n战网群号：818026401\n"))


@game_What.handle()
async def _():
    await game_What.finish(Message("【红色警戒3正版问题解决教程（地图录像mod，汉化，第三方平台联机）-哔哩哔哩】 https://b23.tv/je1PWjR"))


@cdkey.handle()
async def _():
    await cdkey.finish(Message(
        "请访问B站链接进入查看：https://t.bilibili.com/199013810?type=2&comment_on=1&spm_id_from=333.999.rich-text.link.click"))


@arc.handle()
async def _():
    await arc.finish(Message(
        "红色警戒3日冕MOD官网地址 https://cor-games.com/ \n直连下载：http://mtw.so/5MbsnD\n【日冕安装教程-哔哩哔哩】 https://b23.tv/ELwUkLC”"))

@taft.handle()
async def _():
    await taft.finish(Message("1. 防守型塔防：保护目标免受敌人攻击，建造部队和建筑。不限人数。\n2. 进攻图：摧毁敌人目标或全部敌人，禁用部分地图。不限人数。\n3. 闯关图：按指定路线进攻敌人或关卡，通过障碍和挑战完成游戏。不限人数。\n4. 战役图：2-3人游戏，剧情过场动画，与对手进行战斗，任务目标不少于3-4个。\n5. 流线型塔防：在规定道路内设置炮台或单位防御敌方单位，阻止其到达指定地点。不限人数。\n6. 对战图：基地单挑或群批战斗，给予玩家奖励或加成。不限人数。\n7. 娱乐图：以娱乐性质游玩，如三国杀、无限钱等。不限人数。\n8. 执政官图：2v2形式游玩，一人操作运营，另一人操作建造的单位进行攻击敌人等行为。\n9. 海战图：地图区域85%以上为海域范围。\n10. 陆地图：地图区域85%以上为陆地范围。\n11. 虐电图：玩家公平竞争与电脑的战斗。\n12. MOD图：强制使用mod进行游玩，无法通过游戏内传输的地图，适配mod的地图。"))  

@Voice.handle()
async def _():
    await Voice.finish(Message("红警3官方语音包下载地址：http://mtw.so/69qt57\n下载站：http://files.ra3.cc/ra3"))
@tool.handle()
async def _():
    await tool.finish(Message("DirectX_Repair(Enhanced_Edition).exe:https://www.aliyundrive.com/s/8zWEi4tqgDa"))


@netd.handle()
async def _():
    await netd.finish(Message("DirectX_Repair(Enhanced_Edition).exe:https://www.aliyundrive.com/s/8zWEi4tqgDa"))