from abc import ABC, abstractmethod
from typing import List

from course.alfredo.fastapi.webapi.entities import Message


class MessageRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[Message]:
        ...

    @abstractmethod
    def find_by_id(self, message_id: int) -> Message | None:
        ...

    @abstractmethod
    def save(self, message: Message) -> Message:
        ...

    @abstractmethod
    def delete(self, message: Message):
        ...
