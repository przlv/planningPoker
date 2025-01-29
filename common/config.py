from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """
    Класс настроек для чтения переменных окружения
    """

    app_name: str = Field(default="PlanningPoker", alias="APP_NAME")
    app_version: str = Field(default="1.0.0", alias="APP_VERSION")
    path_db: str = Field(default="./planningPoker.db", alias="PATH_DB")
    dev_mode: bool = Field(default=False, alias="DEV_MODE")
    tg_token: str = Field(default="<TOKEN>", alias="TG_TOKEN")


config = Config()
