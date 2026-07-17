from datetime import datetime
from typing import List, Optional

from course.alfredo.fastapi.webapi.models.message import Message
from course.alfredo.fastapi.webapi.services.message_service import MessageService


class MessageServiceMemoryImpl(MessageService):

    def __init__(self):
        self._messages: List[Message] = [
            Message(id=1, text='Hola Mundo Python con fastApi',
                    author_email='andres@correo.com', # type: ignore
                    priority=1),
            Message(id=2, text='Seccion de FastApi en progreso...',
                    author_email=None,
                    priority=3),
            Message(id=3, text='Este es un mensaje de prueba!',
                    author_email='pepe@correo.com', # type: ignore
                    priority=4),
            Message(id=4, text='FastApi con service',
                    author_email='demo@correo.com', # type: ignore
                    priority=1),
            Message(id=5, text='Inversion de control con Depends',
                    author_email='jhon@doe.com', # type: ignore
                    priority=5)
        ]
        self._next_id = 6

    def find_all(self) -> List[Message]:
        # print(f'ID del servicio: {id(self)}')
        return self._messages

    def find_by_id(self, message_id: int) -> Optional[Message]:
        message_found = next((msg for msg in self._messages if msg.id == message_id), None)
        return message_found

    def create(self, new_message: Message) -> Message:
        new_message.id = self._next_id
        self._messages.append(new_message)
        self._next_id += 1
        return new_message

    def update(self, message_id: int, message: Message) -> Optional[Message]:
        for index, msg in enumerate(self._messages):
            if msg.id == message_id:
                update = Message(id=msg.id, text=message.text,
                                 author_email=message.author_email,
                                 priority=message.priority
                                 )
                self._messages[index] = update
                return update
        return None

    def delete(self, message_id: int) -> bool:
        for index, msg in enumerate(self._messages):
            if msg.id == message_id:
                del self._messages[index]
                return True
        return False