from course.alfredo.fastapi.webapi.services.message_service import MessageService
from course.alfredo.fastapi.webapi.services.message_service_memory_impl import MessageServiceMemoryImpl


def get_message_service() -> MessageService:
    return MessageServiceMemoryImpl()