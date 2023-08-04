from playwright.async_api import async_playwright
from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, Message

map = on_fullmatch("战网地图胜率")
cmap = on_fullmatch("战网日冕地图胜率")

@map.handle()
async def _():
    async with async_playwright() as p:
        browser  = await p.chromium.launch()
        c = await browser.new_context(viewport={'width': 500, 'height': 37000})
        page = await c.new_page()
        # page.set_default_navigation_timeout(7000)
        await page.goto('https://ra3battle.net/stats/ra3/1v1/maps')
        await page.locator('.wrapper').screenshot(path='C:/Users/Administrator/Desktop/mapc/weather.png')
        await page.goto('https://ra3battle.net/stats/ra3/1v1/maps?minEloStage=3')
        await page.locator('.wrapper').screenshot(path='C:/Users/Administrator/Desktop/mapc/weather3.png')
        await browser.close()
    data = "地图胜率1000\n"+MessageSegment.image(file="file:///C:/Users/Administrator/Desktop/mapc/weather.png")+"\n地图胜率1200\n"+MessageSegment.image(file="file:///C:/Users/Administrator/Desktop/mapc/weather3.png")
    await map.send(data)

@cmap.handle()
async def _():
    async with async_playwright() as p:
        browser  = await p.chromium.launch()
        c = await browser.new_context(viewport={'width': 700, 'height': 37000})
        page = await c.new_page()
        # page.set_default_navigation_timeout(7000)
        await page.goto('https://ra3battle.net/stats/corona/1v1/maps')
        await page.locator('.wrapper').screenshot(path='C:/Users/Administrator/Desktop/mapc/cweather.png')
        await page.goto('https://ra3battle.net/stats/corona/1v1/maps?minEloStage=3')
        await page.locator('.wrapper').screenshot(path='C:/Users/Administrator/Desktop/mapc/cweather3.png')
        await browser.close()
    data = "地图胜率1000\n"+MessageSegment.image(file="file:///C:/Users/Administrator/Desktop/mapc/cweather.png")+"\n地图胜率1200\n"+MessageSegment.image(file="file:///C:/Users/Administrator/Desktop/mapc/cweather3.png")
    await cmap.send(data)