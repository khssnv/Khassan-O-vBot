from typing import Set

from pydantic import BaseSettings


class TelegramClientCredentials(BaseSettings):
    session: str
    api_id: int
    api_hash: str

    class Config:
        env_prefix = "TELEGRAM_CLIENT_"
        case_sensitive = False


class TelegramBotCredentials(BaseSettings):
    token: str

    class Config:
        env_prefix = "TELEGRAM_BOT_"


class Settings(BaseSettings):
    me: int
    aggregation_channel: str
    aggregated_chats: Set[str]
    tgclient_creds: TelegramClientCredentials
    tgbot_creds: TelegramBotCredentials

    class Config:
        env_prefix = "TELEGRAM_"
        case_sensitive = False


settings = Settings(
    tgclient_creds=TelegramClientCredentials(), tgbot_creds=TelegramBotCredentials()
)
print(settings)
