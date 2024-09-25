from pydantic import BaseModel


class ConfigModel(BaseModel):
    pjsk_plugin_enabled: bool = True
    monitored_group: list = []
    update_music : bool = False

