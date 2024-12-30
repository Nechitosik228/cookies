from .models import (
    Config,
    Task
)


def up():
    Config.BASE.metadata.create_all(Config.ENGINE)


def down():
    Config.BASE.metadata.drop_all(Config.ENGINE)


def migrate():
    down()
    up()





