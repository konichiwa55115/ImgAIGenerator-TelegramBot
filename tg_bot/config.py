from environs import Env

from dataclasses import dataclass

@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str
    port: str 


@dataclass
class TgBot:
    token: str
    admin_ids: int
    use_redis: True

@dataclass
class Miscellaneous:
    other_params: str = None

@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc = Miscellaneous



def load_config(path: str = None):
    env = Env()
    env.read_env(path)


  
