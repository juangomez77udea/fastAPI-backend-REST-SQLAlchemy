from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from course.juan.fastapi.webapi.config.db import SessionLocal
from course.juan.fastapi.webapi.repositories.message_repository import MessageRepository
from course.juan.fastapi.webapi.repositories.sql_alchemy_message_repository import SQLAlchemyMessageRepository
from course.juan.fastapi.webapi.services.message_service import MessageService
from course.juan.fastapi.webapi.services.sql_message_service import SQLAlchemyMessageService


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_message_repository(db: Session = Depends(get_db)) -> MessageRepository:
    return SQLAlchemyMessageRepository(db)

def get_message_service(
        db: Session = Depends(get_db),
        repo: MessageRepository = Depends(get_message_repository)) -> MessageService:
    return SQLAlchemyMessageService(repo, db)