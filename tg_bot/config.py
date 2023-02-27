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
    admin_ids: list[int]
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


    return Config(
        tg_bot=TgBot(
            token="6169974916:AAFO4oyy5fiYM19VrLiJ0lyc-MN9gCFVgd0",
            admin_ids=int(6234365091),
            use_redis=False,
        ),
        db=DbConfig(
            host="db.ocsrfwsqoiuztsqyjbip.supabase.co",
            password="Ibntaymya1.",
            user="postgres",
            database="postgres",
            port=int(5432)
        ),
        # misc=Miscellaneous()
    )
