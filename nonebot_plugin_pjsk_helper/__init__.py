from nonebot.plugin import PluginMetadata
from .config import Config
from .import __main__ as __main__

__version__ = "1.0.7"
__plugin_meta__ = PluginMetadata(
    name="pjsk-helper",
    description="基于 Nonebot2 的 Project Sekai 助手",
    usage="使用命令 pjsk help 查看帮助",
    type="application",
    homepage="https://github.com/Atr1ck/nonebot-plugin-pjsk-helper",
    supported_adapters={"~onebot.v11"},
    config=Config,
)