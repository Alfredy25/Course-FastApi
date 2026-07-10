from typing import List

from fastapi import APIRouter

from course.alfredo.fastapi.webapi.models.message import Message

sample_messages: List[Message] = [
    Message(id=1, text='Hola Mundo Python con fastApi'),
    Message(id=2, text='Seccion de FastApi en progreso...'),
    Message(id=3, text='Este es un mensaje de prueba!')
]

router = APIRouter()

@router.get("/", response_model=List[Message])
def list_messages():
    return sample_messages