from pydantic import BaseModel


class Config(BaseModel):
    pjsk_plugin_enabled: bool = True
    monitored_group: list = []

