from environs import Env
from flask import Flask

env = Env()
env.read_env()


def init_app(app: Flask):
    app.config["JSON_SORT_KEYS"] = env("JSON_SORT_KEYS")
    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLA_DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = env("SQLA_TRACK_MOD")