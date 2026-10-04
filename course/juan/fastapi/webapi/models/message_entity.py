from dataclasses import dataclass


@dataclass
class MessageEntity:
    id: int
    text: str
    secret: str