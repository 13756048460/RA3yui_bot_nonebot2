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
yp = on_fullmatch("塔防语音链接")
taft = on_fullmatch("红3地图分类")
mod_Don = on_fullmatch("mod列表")
Voice = on_fullmatch("红警3语音包")
tool = on_fullmatch("dx修复工具")



@mod_Don.handle()
async def _():
    await mod_Don.finish(MessageSegment.text("-------------------------"+"\n"+"Insurrection:群453239661"+"\n"+"科学MOD:群603768052"+"\n"+"最终协议:群953437366"+"\n"+"Armor Rush:群622692891"+"\n"+"沙雕警戒3:群948371257"+"\n"+"龙霸天下:群150559741 群213356762"+"\n"+"将军2:群296524582"+"\n"+"The New World:群299420109"+"\n"+"Remix:群787717922"+"\n"+"冲突世界:群577591891"+"\n"+"复兴:群151512582"+"\n"+"Psyonic Omega:群334579291"+"\n"+"Dawn黎明MOD:群499406325"+"\n"+"Eisenreich:群653952489"+"\n"+"ChaosFA:群165624222"+"\n"+"强权战争:群891321634 群684025988"+"\n"+"幻次元:群902670452"+"\n"+"宿敌:群837758987"+"\n"+"崩坏3:群832289938"+"\n"+"塔防大师:群915031091 群652469807"+"\n"+"FS+TCB:群689669808"+"\n"+"尤里归来:群1081649797"+"\n"+"二重进化:群1043277809"+"\n"+"TECH-SHUFFLE（科技重组MOD）:群249748868"+"\n"+"日冕Corona:群853481766"+"\n"+"德意志同盟中央歌剧院:群801141387"+"\n"+"战时联合:群781467431"+"\n"+"地狱行军:群675257891"+"\n"+"回春:群727525312"+"\n"+"Uprising Reborn:群701203945"+"\n"+"猫球警戒:群854509748"+"\n"+"RAC:群600926742"+"\n"+"Bugbits群：854595269"+"\n"+"-------------------------"))
# @mod_Don.handle()
# async def _():
#     await mod_Don.finish(Message("-------------------------"+"\n"+"查看群聊请查看此腾讯文档："+"\n"+"https://docs.qq.com/doc/DWUtlRkVoWG9EQWdZ"+"\n"+"-------------------------"))


@ra3.handle()
async def _():
    await ra3.finish(Message("命令与征服：红色警戒3原版加群：607024829 \n 命令与征服：红色警戒3阉割版.exe:https://www.aliyundrive.com/s/byVZzf969BS\n此压缩包文件是由小琪打包完成的\n红3bwiki网站：https://wiki.biligame.com/redalert3 \n 红警3原版下载链接:https://cowtransfer.com/s/38ff9aff587946"))


@ra3up.handle()
async def _():
    await ra3up.finish(Message("命令与征服：红色警戒3起义时刻与起义时刻电影包加群：1098605891 \n 红警3起义时刻下载链接：https://cowtransfer.com/s/ed39e1e4009d49"))


@mapd.handle()
async def _():
    await mapd.finish(Message(
        "作者：橘子皮\n红色警戒3地图上传下载管理器正式版公测，注册账号后可以上传更新管理自制地图。凡是地图方面的内容基本上都有了，如果各位有什么地图方面的建议可以在软件上进行建议投稿。\n群1: 953371430\n群验证密码：免费软件付费举报商家\n红警3（地图工具）频道QQ频道号：5mv9jv6nvf \n红警3地图百科:http://wu162.gitee.io/ra3mapwiki/zh/，地编新版研究群：613550502 \n地图下载工具使用视频教程：https://www.bilibili.com/video/BV16L411h7oN \nRA3地图下载工具3.68.exe：https://www.aliyundrive.com/s/dMuonauGDMW"))

@RA3BattleNet.handle()
async def _():
    await RA3BattleNet.finish(Message(
        "战网正式版已于2023.3.23日晚上开始正式上线。目前支持1v1匹配，战役联机，好友添加，对战排行，执政官匹配，人机匹配，卡比延迟检测等功能，也是目前的主流红警3联机平台，更多介绍可以访问战网官网浏览。请注意作为一位独一无二的战网用户，您将会作为一名“用户”使用战网服务，您每次在战网上使用的用户名将会被称作“账号”，每个账号可以使用任意多个在线ID（又称“马甲”），每位“用户”可以使用无限个“账号”。如果战网要对账号作出相应的封禁处罚，则为该账号无法使用相应天数，而用户可以创建其他账号继续使用，封号处罚力度：1天、3天、7天、永久封禁。而如果战网要对用户做出封禁处罚，则该用户的所有账号都会被封禁，该用户在封禁期间将会无法被使用战网。\n战网官网：https://ra3battle.net\n 战网联机使用视频教程：https://www.bilibili.com/video/BV16L411h7oN \n战网群号：604807102"))


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
        "红色警戒3日冕MOD正式公测！公测官网地址 https://cor-games.com/\n直连下载：https://cf.file.rmrts.com/srv/cor/launcher/CoronaLauncher_Setup_3.7.8420.37088.exe\n【日冕安装教程-哔哩哔哩】 https://b23.tv/ELwUkLC”"))

@yp.handle()
async def _():
    await yp.finish(Message("https://kook.top/jsTLSS"))

@taft.handle()
async def _():
    await taft.finish(Message("1.防守型塔防：玩家需要在固定地图上建造部队和建筑，来保护任务目标免受敌人的攻击一般情况下不受人数限制。\n2.进攻图：玩家需要进攻并摧毁敌人的某个目标或全部敌人，可以使用各种东西来达成胜利。（部分地图会进行禁用）一般情况下不受人数限制。\n3.闯关图：玩家需要按照指定路线顺序依次进攻敌人或关卡，并且需要通过各种障碍和挑战来完成游戏一般情况下不受人数限制。\n4.战役图：通常为2-3人游戏，带有剧情过场动画，玩家需要与对手进行战斗，以获得胜利。并且一般情况下任务目标不少于3-4个。\n5.流线型塔防：玩家需要在规定的道路内设置炮台或者单位来防御敌方单位，并且主要目的是为阻止敌方单位到达指定地点，一般情况敌人都会按照设置好的路线前进，一般情况不受人数限制.\n6.对战图：玩家开局基本上只有一个基地来进行单挑或者群批为主的战斗，可以适当给玩家双方一些奖励或者加成，不存在说一方过强。\n7.娱乐图：玩家一般会以娱乐的性质来进行游玩，举例包括（三国杀，小块地，无限钱，箱子图），还有刷兵来进行游玩的图和禁用一些单位（空战步兵战坦克战海军战）之间玩家对战的图也属于娱乐图范围。\n8.执政官图：玩家一般情况都是2v2形式游玩，也有小部分其他特殊情况，具体可以地图作者在介绍写清楚，玩家一人操作运营（包括建筑，工程师，协议的使用），另一人操作运营方建造的单位来进行使用和攻击敌人等行为。\n9.海战图：指地图区域百分之85以上都是海域范围称为海战图。\n10.陆地图：指地图区域百分之85以上都是陆地范围成为陆战图。\n11.虐电图：指地图作者主要想以玩家公平竞争电脑开局之间的战斗。\n12.MOD图：指玩家需要强制使用的mod进行游玩，还有无法通过游戏内传输的地图，最后还有针对mod进行适配的图统称为MOD图。"))  

@Voice.handle()
async def _():
    await Voice.finish(Message("红警3官方语音包下载地址：https://www.aliyundrive.com/s/8xt6ajFoeDe"))

@tool.handle()
async def _():
    await tool.finish(Message("DirectX_Repair(Enhanced_Edition).exe:https://www.aliyundrive.com/s/8zWEi4tqgDa"))                    
