from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from .config import Config


class Task(Config.BASE):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
