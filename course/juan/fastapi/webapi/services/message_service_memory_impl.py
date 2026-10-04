from typing import List, Optional

from course.juan.fastapi.webapi.models.messages import Message
from course.juan.fastapi.webapi.services.message_service import MessageService


class MessageServiceMemoryImpl(MessageService):

    def __init__(self):
        self._messages: List[Message] = [
            Message(id=1, text="Hola mundo python con fastApi", author_email='andres@example.com', priority=1),
            Message(id=2, text="Sección de fastApi", author_email=None, priority=3),
            Message(id=3, text="Este es un mensaje de prueba", author_email='pep@example.com', priority=4),
            Message(id=4, text="FastApi con service", author_email='demo@example.com',priority=1),
            Message(id=5, text="Inversión de control con Depends", author_email='jhon@example.com', priority=5),
        ]
        self._next_id = 6

    def find_all(self) -> List[Message]:
        #print(f'Id del servicio: {id(self)}')
        return self._messages

    def find_by_id(self, message_id: int) -> Optional[Message]:
        return next((msg for msg in self._messages if msg.id == message_id), None)

    def create_message(self, new_message: Message) -> Message:
        new_message.id = self._next_id
        self._messages.append(new_message)
        self._next_id += 1
        return new_message

    def update(self, message_id: int, message: Message) -> Optional[Message]:
        for index, msg in enumerate(self._messages):
            if msg.id == message_id:
                updated = Message(id=message_id,
                                  text=message.text,
                                  author_email=message.author_email,
                                  priority=message.priority)
                self._messages[index] = updated
                return updated
        return None

    def delete(self, message_id: int) -> bool:
        for index, msg in enumerate(self._messages):
            if msg.id == message_id:
                del self._messages[index]
                return True
        return False