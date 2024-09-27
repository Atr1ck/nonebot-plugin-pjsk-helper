<!-- markdownlint-disable MD024 MD026 MD031 MD033 MD036 MD041 -->

<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/Agnes4m/nonebot_plugin_l4d2_server/main/image/logo.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/plugin.svg" alt="NoneBotPluginText">
</p>

# ✨-Project Sekai Helper-✨

</div>

## 💬 前言
- 本插件仅用于学习交流使用，请勿用于商业用途(虽然应该也没什么商业用途(x，如有侵权请联系我删除
- 其实本来希望能读取玩家数据之类的，结果发现SEGA在23年把这个接口关了(😡
## 🔧安装
<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 nonebot2 项目的根目下打开命令行, 输入以下指令即可安装 

```bash
nb plugin install nonebot-plugin-pjsk-helper
```

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

```bash
pip install nonebot-plugin-pjsk-helper
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add nonebot-plugin-pjsk-helper
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add nonebot-plugin-pjsk-helper
```

</details>
<details>
<summary>conda</summary>

```bash
conda install nonebot-plugin-pjsk-helper
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_pjsk"
]
```

</details>

## 📚使用说明

### 指令
```qq
/pjsk card [team][name][type] 根据参数随机获取角色卡卡面
```     
- team - 各队伍名

队伍名与简称的对应关系如下⬇️:
| 队伍 | 简称 |
|:----:|:----:|
|Leo/need| ln |
|More More Jump| mmj |
|Vivid Bad Sqaud| vbs |
|Wonderland Showtime| ws|
|Vitrual Singer| vs |
- name - 各角色名

角色本名与简称对应关系如下⬇️:

|   人名       | 简称  |
|:-----------:|:------:|
| 星乃 一歌   | ick   |
| 天马 咲希   | saki  |
| 望月 穗波   | hnm   |
| 日野森 志步 | shino |
| 花里 实乃里 | mnr   |
| 桐谷 遥     | hrk   |
| 桃井 爱莉   | airi  |
| 日野森 雫   | szk   |
| 小豆泽 心羽 | khn   |
| 白石 杏     | an    |
| 东云 彰人   | akt   |
| 青柳 冬弥   | toya  |
| 天马 司     | tks   |
| 凤 笑梦     | emu   |
| 草薙 宁宁   | nene  |
| 神代 类     | rui   |
| 宵崎 奏     | knd   |
| 朝比奈 真冬 | mfy   |
| 东云 绘名   | ena   |
| 晓山 瑞希   | mzk   |
| 初音 未来   | miku  |
| 镜音 铃     | rin   |
| 镜音 连     | ren   |
| 巡音 流歌   | ruka  |
| MEIKO       | meiko |
| KAITO       | kaito |

- type - 卡片类型,可取"normal","train"

若上述三个参数错误则会**忽略**该项参数

优先级 **人物 > 队伍**

```qq
/pjsk update music/card
```
- 更新曲库/卡面

```qq
/pjsk music difficulty name/id
```

| 参数 | 值 |
|:---:|:----:|
|difficulty|easy, normal, hard, expert, master, [apppend]|
|name | 歌曲名，例如 相生, 快晴|
|id   | 歌曲id, 目前在data文件夹下pjsk_music.json无序列出|

```qq
/pjsk help
```
- 发送使用说明


### 配置
|      配置项       |  必填   |  默认值  |               说明            |
|:----------------:|:------:|:--------:|:---------------------------:|
|PJSK_PLUGIN_ENABLED|  否    | True    | 是否开启插件 |
|  MONITORED_GROUP |   否    | []      | 选定插件管理的群聊，若为默认值则所有管理所有群聊|

## ⚠️注意
- 使用update指令时会有网页出现，虽然尝试无头启动但会导致无法正常运行(x
- 目前仅支持chromium内核，其他尚未添加与测试
## 🙏鸣谢
- 本插件数据来源[Sekai Viewer](https://sekai.best/)

## ☎联系
如有任何bug可直接在仓库提issue或以下列方式联系我:
- E-mail : 3126670240@qq.com 
- QQ: 3126670240

## To Do List
- 优化update指令
- 添加新功能(还没想好 :|

## 📝更新日志

### 1.0.3
- 优化updatei指令:
  - 更换selenium为playwright, 实现更好的异步
  - 实现无头启动
- 修复music指令的读取bug

### 1.0.2

- 修复update指令bug
  - 修正ChromeDriverManager的使用
  - 更改函数为异步，防止阻塞其他函数的使用
  - 修正依赖，添加lxml

### 1.0.0

- 完成README文档，插件正式上线