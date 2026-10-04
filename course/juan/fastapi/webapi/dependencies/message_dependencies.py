from course.juan.fastapi.webapi.config.db import SessionLocal
from course.juan.fastapi.webapi.services.message_service import MessageService
from course.juan.fastapi.webapi.services.message_service_memory_impl import MessageServiceMemoryImpl
from functools import lru_cache

@lru_cache()
def get_message_service() -> MessageService:
    return MessageServiceMemoryImpl()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()