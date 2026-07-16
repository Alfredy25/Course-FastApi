from fastapi import Depends
from sqlalchemy.orm import Session

from course.alfredo.fastapi.webapi.config.db import SessionLocal
from course.alfredo.fastapi.webapi.repositories.message_repository import MessageRepository
from course.alfredo.fastapi.webapi.repositories.sql_alchemy_message_repository import SQLAlchemyMessageRepository
from course.alfredo.fastapi.webapi.services.message_service import MessageService
from course.alfredo.fastapi.webapi.services.sql_alchemy_message_service import SQLAlchemyMessageService


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_message_repository(db: Session = Depends(get_db)) -> MessageRepository:
    return SQLAlchemyMessageRepository(db)

def get_message_service(repo: MessageRepository = Depends(get_message_repository),
                        db: Session = Depends(get_db)) -> MessageService:
    return SQLAlchemyMessageService(repo, db)