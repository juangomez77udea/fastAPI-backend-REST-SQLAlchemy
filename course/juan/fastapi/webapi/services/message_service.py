from abc import ABC, abstractmethod
from typing import List, Optional

from course.juan.fastapi.webapi.models.messages import Message


class MessageService(ABC):
    @abstractmethod
    def find_all(self) -> List[Message]:
        ...

    @abstractmethod
    def find_by_id(self,  message_id: int) -> Optional[Message]:
        ...
    @abstractmethod
    def create_message(self, new_message: Message) -> Message:
        ...

    @abstractmethod
    def update(self, message_id: int, message: Message) -> Optional[Message]:
        ...

    @abstractmethod
    def delete(self, message_id: int) -> bool:
        ...

