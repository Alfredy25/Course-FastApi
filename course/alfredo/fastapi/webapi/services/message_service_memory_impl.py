from typing import List, Optional

from course.alfredo.fastapi.webapi.models.message import Message
from course.alfredo.fastapi.webapi.services.message_service import MessageService


class MessageServiceMemoryImpl(MessageService):
    def __init__(self):
        self._messages: List[Message] = [
            Message(id=1, text='Hola Mundo Python con fastApi'),
            Message(id=2, text='Seccion de FastApi en progreso...'),
            Message(id=3, text='Este es un mensaje de prueba!'),
            Message(id=4, text='FastApi con service'),
            Message(id=5, text='Inversion de control con Depends'),
        ]

    def find_all(self) -> List[Message]:
        # print(f'ID del servicio: {id(self)}')
        return self._messages

    def find_by_id(self, message_id: int) -> Optional[Message]:
        message_found = next((msg for msg in self._messages if msg.id == message_id), None)
        return message_found