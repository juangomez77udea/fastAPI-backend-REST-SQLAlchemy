from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from course.juan.fastapi.webapi.config.db import Base


class Message(Base):
    __tablename__ = "message"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(200), nullable=False)
    author_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    priority: Mapped[int] = mapped_column(Integer, nullable=False, default=1)