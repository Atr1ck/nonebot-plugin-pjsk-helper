from bs4 import BeautifulSoup
from .config import Config
from nonebot import get_plugin_config
from playwright.async_api import async_playwright
from pathlib import Path
import re
import json

current_dir = Path(__file__).resolve().parent

config = get_plugin_config(Config)

async def scroll_and_wait(page):
    # 获取页面的初始高度
    last_height = await page.evaluate("document.body.scrollHeight")

    while True:
        # 滚动到页面底部
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

        # 等待页面加载
        await page.wait_for_timeout(1000)  # 等待1秒
        
        # 重新获取页面高度
        new_height = await page.evaluate("document.body.scrollHeight")
        
        # 如果页面高度不变，说明加载完成
        if new_height == last_height:
            break
        last_height = new_height

async def update_music():
    url = 'https://sekai.best/music'
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await scroll_and_wait(page)
        html = await page.content()
        await browser.close()
    soup = BeautifulSoup(html, "lxml")
    music_info = []
    for item in soup.find_all("div", class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-3 MuiGrid-grid-xl-3 css-1etv89n"):
        try:
            music_id_path = item.find("a")["href"]
            match = re.search(r'\d+', music_id_path)
            music_id = match.group()

            music_name = item.find("div", class_="MuiCardMedia-root css-bc9mfn")["title"].split("|")[0].strip()
            
            music_cover_raw=  item.find("div", class_="MuiCardMedia-root css-bc9mfn")["style"]
            music_cover_webp_re = re.search(r'url\("(.*?)"\)', music_cover_raw)
            music_cover_webp = music_cover_webp_re.group(1)
            music_cover_png = music_cover_webp.replace('.webp', '.png')

            music_info.append({
                "music_id":music_id,
                "music_name":music_name,
                "music_cover_png":music_cover_png
            })
        except:
            break
    with open(f"{current_dir}/data/pjsk_music.json", "w",encoding="UTF-8") as json_file:
        json.dump(music_info, json_file, ensure_ascii=False, indent=4)