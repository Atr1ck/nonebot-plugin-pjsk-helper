from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment, Message
from nonebot.params import CommandArg
import random
import json
from pathlib import Path
from . import music_find, music_data_get, character_data_get
from nonebot import get_plugin_config
from .config import Config

current_dir = Path(__file__).resolve().parent
config = get_plugin_config(Config)

pjsk_card = on_command("pjsk card")
pjsk_music = on_command("pjsk music")
pjsk_update = on_command("pjsk update")
pjsk_help = on_command("pjsk help")

@pjsk_update.handle()
async def hanlde_pjsk_update_card(bot: Bot, event: GroupMessageEvent, args: Message = CommandArg()):
    arg_text = args.extract_plain_text().strip()
    if arg_text == "card":
        await character_data_get.update_character()
    elif arg_text == "music":
        await music_data_get.update_music()
    else:
        await bot.send_group_msg(group_id=event.group_id, message="参数错误，请重试")

@pjsk_card.handle()
async def handle_psjk_card(bot: Bot, event: GroupMessageEvent, args: Message = CommandArg()):
    if config.pjsk_plugin_enabled == False:
        print("插件已关闭")
        return
    group_id = event.group_id  
    if group_id not in config.monitored_group and config.monitored_group != []:
        return 
    arg_text = args.extract_plain_text().strip()

    team = None
    spe_character = None
    card_type = None
    for arg in list(arg_text.split()):
        if arg in ["ln","mmj","vbs","ws","25s","vs"]:
            team = arg
        elif arg in ["normal", "train"]:
            card_type = "normal" if arg == "normal" else "after_training"
        else:
            spe_character = arg
    
    # await bot.send_group_msg(group_id=group_id,message=MessageSegment.at(event.user_id) + " 正在获取卡面，请稍等")
    with open(f"{current_dir}/data/pjsk_character.json", "r", encoding="UTF-8") as json_file:
        character_info = json.load(json_file)
    
    if not card_type:
        card_type = random.choice(["normal", "after_training"])
    chara_id_min = 1
    chara_id_max = 26
    if team:
        for character in character_info:
            if team == character["team"]:
                chara_id_min = character["id"]
                chara_id_max = chara_id_min + 3 + int(team == "vs")
                break
    
    chara_id = None
    if spe_character:
        chara_id = [i for i in character_info if i["name"] == spe_character][0]["id"]
    
    if not chara_id:
        chara_id = random.randint(chara_id_min, chara_id_max)
    
    pic_id = random.randint(1, int([i for i in character_info if i["id"] == chara_id][0]["counts"]))
    png_url = f"https://storage.sekai.best/sekai-jp-assets/character/member/res{chara_id:03}_no{pic_id:03}_rip/card_{card_type}.png"
    for i in range(3):
        try:
            await bot.send_group_msg(group_id=group_id, message=MessageSegment.image(png_url))
            break
        except Exception as e:
            print(e)
            print("正在重新抽取")
            pic_id = random.randint(1, int([i for i in character_info if i["id"] == chara_id][0]["counts"]))
            png_url = f"https://storage.sekai.best/sekai-jp-assets/character/member/res{chara_id:03}_no{pic_id:03}_rip/card_{card_type}.png"
    else:
        print("发送失败")

@pjsk_music.handle()
async def pjsk_music(bot:Bot, event: GroupMessageEvent, args: Message = CommandArg()):
    if config.pjsk_plugin_enabled == False:
        print("插件已关闭")
        return
    group_id = event.group_id
    with open(f"{current_dir}/data/pjsk_music.json", "r", encoding="UTF-8") as json_file:
        music_info = json.load(json_file)

    arg_text = args.extract_plain_text().strip()
    difficulty, music_idorname= arg_text.split(" ")

    if difficulty not in ["easy", "normal", "hard", "expert", "master", "append"]:
        await bot.send_group_msg(group_id=group_id, message="难度输入错误，请重试")
        return
    elif music_idorname.isdigit():
        music = music_find.find_by_music_id(music_idorname, music_info)
        if not music:
            await bot.send_group_msg(group_id=group_id, message="id输入错误")
            return
    else:
        music = music_find.find_by_music_name(music_idorname, music_info)
        if not music:
            await bot.send_group_msg(group_id=group_id, message="歌曲名输入错误")
            return
    
    music_id = int(music["music_id"])
    music_sheet = f"https://storage.sekai.best/sekai-music-charts/jp/{music_id:04}/{difficulty}.png"
    message = f'歌曲名: {music["music_name"]}\n' + f'歌曲id: {music["music_id"]}' + MessageSegment.image(music["music_cover_png"]) + "\n" + f'难度:{difficulty}\n'
    try:
        message1 = message + MessageSegment.image(music_sheet)
        await bot.send_group_msg(group_id=group_id, message=message1)
    except:
        message2 = message + "暂无该谱"
        await bot.send_group_msg(group_id=group_id, message=message2)

@pjsk_help.handle()
async def pjsk_help_handle(bot:Bot, event:GroupMessageEvent):
    group_id = event.group_id
    helpinfo = '''
    所有指令统一以pjsk为前缀

    card [team][name][type]     team - 各队伍名,可取"ln","mmj","vbs","ws","vs"
                                name - 各角色名,可取"ick","saki","hnm","shino","mnr","hrk","airi","szk","khn","an","akt","toya","tks",
                                                  "emu","nene","rui","knd","mfy","ena","mzk","miku","rin","ren","ruka","meiko","kaito"
                                type - 卡片类型,可取"normal","train"
                                若参数错误则会忽略该参数

    update music/card           更新曲库/卡面

    music difficulty name/id    difficulty - 难度，可从"easy","normal","hard","expert","master",个别歌曲有"append"
                                name/id w- 歌曲名/歌曲id
    '''

    if config.monitored_group == [] or group_id in config.monitored_group:
        await bot.send_group_msg(group_id=group_id,message=MessageSegment.image(f"file://{current_dir}/data/help.png"))