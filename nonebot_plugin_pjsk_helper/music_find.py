def find_by_music_id(music_id, music_info):
    for music in music_info:
        if music['music_id'] == music_id:
            return music
    return False  # 如果没有找到，返回 None

# 根据 music_name 查询
def find_by_music_name(music_name, music_info):
    for music in music_info:
        if music['music_name'] == music_name:
            return music
    return False  # 如果没有找到，返回 None