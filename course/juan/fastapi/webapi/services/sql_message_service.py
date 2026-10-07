from typing import List, Optional

from sqlalchemy.orm import Session

from course.juan.fastapi.webapi.entities.message import Message as MessageEntity
from course.juan.fastapi.webapi.models.messages import Message as MessageDto
from course.juan.fastapi.webapi.repositories.message_repository import MessageRepository
from course.juan.fastapi.webapi.services.message_service import MessageService


class SQLAlchemyMessageService(MessageService):
    def __init__(self, repo: MessageRepository, db: Session):
        self._repo = repo
        self._db = db

    def find_all(self) -> List[MessageDto]:
        return [self._to_dto(message_entity) for message_entity in self._repo.find_all()]

    def find_by_id(self, message_id: int) -> Optional[MessageDto]:
        entity = self._repo.find_by_id(message_id)
        if not entity:
            return None
        return self._to_dto(entity)

    def create_message(self, new_message: MessageDto) -> MessageDto:
        entity = MessageEntity(
            text=new_message.text,
            author_email=new_message.author_email,
            priority=new_message.priority
        )
        try:
            saved = self._repo.save(entity)
            self._db.commit()
            self._db.refresh(saved)
            return self._to_dto(saved)
        except Exception:
            self._db.rollback()
            raise

    def update(self, message_id: int, message: MessageDto) -> Optional[MessageDto]:
        entity = self._repo.find_by_id(message_id)
        if entity is None:
            return None
        entity.text = message.text
        entity.author_email = message.author_email
        entity.priority = message.priority
        try:
            self._repo.save(entity)
            self._db.commit()
            self._db.refresh(entity)
            return self._to_dto(entity)
        except Exception:
            self._db.rollback()
            raise

    def delete(self, message_id: int) -> bool:
        entity = self._repo.find_by_id(message_id)
        if entity is None:
            return False
        try:
            self._repo.delete(entity)
            self._db.commit()
            return True
        except Exception:
            self._db.rollback()
            raise

    @staticmethod
    def _to_dto(entity: MessageEntity) -> MessageDto:
        return MessageDto.model_validate(entity, from_attributes=True)