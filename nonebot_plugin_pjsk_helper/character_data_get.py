from bs4 import BeautifulSoup
from .config import Config
from nonebot import get_plugin_config
from .music_data_get import scroll_and_wait
from playwright.async_api import async_playwright
from pathlib import Path
import json

current_dir = Path(__file__).resolve().parent

character_map = {
    "星乃 一歌":["ln","ick",1],
    "天马 咲希":["ln","saki",2],
    "望月 穗波":["ln","hnm",3],
    "日野森 志步":["ln","shino",4],
    "花里 实乃里":["mmj","mnr",5],
    "桐谷 遥":["mmj","hrk",6],
    "桃井 爱莉":["mmj","airi",7],
    "日野森 雫":["mmj","szk",8],
    "小豆泽 心羽":["vbs","khn",9],
    "白石 杏":["vbs","an",10],
    "东云 彰人":["vbs","akt",11],
    "青柳 冬弥":["vbs","toya",12],
    "天马 司":["ws","tks",13],
    "凤 笑梦":["ws","emu",14],
    "草薙 宁宁":["ws","nene",15],
    "神代 类":["ws","rui",16],
    "宵崎 奏":["25h","knd",17],
    "朝比奈 真冬":["25h","mfy",18],
    "东云 绘名":["25h","ena",19],
    "晓山 瑞希":["25h","mzk",20],
    "初音 未来":["vs","miku",21],
    "镜音 铃":["vs","rin",22],
    "镜音 连":["vs","ren",23],
    "巡音 流歌":["vs","ruka",24],
    "MEIKO":["vs","meiko",25],
    "KAITO":["vs","kaito",26]
}

config = get_plugin_config(Config)

async def update_character():
    url = 'https://sekai.best/card'
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await scroll_and_wait(page)
        html = await page.content()
        with open(f"{current_dir}/data/html.txt", "w") as f:
            f.write(html)
        await browser.close()
    soup = BeautifulSoup(html, "lxml")
    card_counts = [0] * 26
    character_info = []
    for item in soup.find_all("p", class_="MuiTypography-root MuiTypography-body2 css-1wtd2mf"):
        try:
            try:
                character_name = item.text.split("|")[1].strip()
            except:
                character_name = item.text.strip()
            
            card_counts[character_map[character_name][2]-1] += 1

        except:
            break
    
    for character in character_map.values():
        character_info.append(
            {
                "team" : character[0],
                "name" : character[1],
                "id" : character[2],
                "counts" : card_counts[character[2]-1]
            }
        )

    with open(f"{current_dir}/data/pjsk_character.json", "w",encoding="UTF-8") as json_file:
        json.dump(character_info, json_file, ensure_ascii=False, indent=4)