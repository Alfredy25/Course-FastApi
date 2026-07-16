from typing import Optional, List

from sqlalchemy.orm import Session
from course.alfredo.fastapi.webapi.models.message import Message as MessageDto
from course.alfredo.fastapi.webapi.entities.message import Message as MessageEntity
from course.alfredo.fastapi.webapi.repositories.message_repository import MessageRepository
from course.alfredo.fastapi.webapi.services.message_service import MessageService


def entity_to_dto(entity: MessageEntity) -> MessageDto:
    return MessageDto.model_validate({
        'id': entity.id,
        'text': entity.text,
        'author_email': entity.author_email,
        'priority': entity.priority
    })


class SQLAlchemyMessageService(MessageService):
    def __init__(self, repo: MessageRepository, db: Session):
        self._repo = repo
        self._db = db

    def find_all(self) -> List[MessageDto]:
        return [entity_to_dto(message_entity) for message_entity in self._repo.find_all()]

    def find_by_id(self, message_id: int) -> Optional[MessageDto]:
        entity = self._repo.find_by_id(message_id)
        if not entity:
            return None
        return entity_to_dto(entity)

    def create(self, new_message: MessageDto) -> MessageDto:
        entity = MessageEntity(
            text=new_message.text,
            author_email=new_message.author_email,
            priority=new_message.priority,
        )
        try:
            obj_saved = self._repo.save(entity)
            self._db.commit()
            self._db.refresh(obj_saved)
            return entity_to_dto(entity)
        except Exception:
            self._db.rollback()
            raise

    def update(self, message_id: int, message: MessageDto) -> Optional[MessageDto]:
        entity = self._repo.find_by_id(message_id)
        if not entity:
            return None
        entity.text = message.text
        entity.author_email = message.author_email
        entity.priority = message.priority
        try:
            self._db.commit()
            self._db.refresh(entity)
            return entity_to_dto(entity)
        except Exception:
            self._db.rollback()
            raise

    def delete(self, message_id: int) -> bool:
        entity = self._repo.find_by_id(message_id)
        if not entity:
            return False

        try:
            self._repo.delete(entity)
            self._db.commit()
            return True
        except Exception:
            self._db.rollback()
            raise