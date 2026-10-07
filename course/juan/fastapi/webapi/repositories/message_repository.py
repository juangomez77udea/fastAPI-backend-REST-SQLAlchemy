from abc import ABC, abstractmethod
from typing import List, Optional

from course.juan.fastapi.webapi.entities.message import Message


class MessageRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Message]:
        ...

    @abstractmethod
    def find_by_id(self, message_id: int) -> Optional[Message]:
        ...

    @abstractmethod
    def save(self, message: Message) -> Message:
        ...

    @abstractmethod
    def delete(self, message: Message) -> None:
        ...