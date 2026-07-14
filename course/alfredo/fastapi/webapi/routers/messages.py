"""
El router debe encargarse principalmente de cosas HTTP:
    * Definir rutas.
    * Recibir parámetros.
    * Recibir body JSON.
    * Validar entrada con modelos.
    * Llamar al servicio correcto.
    * Devolver respuesta.
    * Lanzar errores HTTP cuando aplique.

El router no debería tener directamente lógica pesada de negocio.
"""

from typing import List, Optional
from fastapi import APIRouter, Depends, Query

from course.alfredo.fastapi.webapi.dependencies.message_dependencies import get_message_service
from course.alfredo.fastapi.webapi.models.message import Message
from course.alfredo.fastapi.webapi.services.message_service import MessageService

router = APIRouter()

@router.get("/", response_model=List[Message])
def list_messages(service: MessageService = Depends(get_message_service)):
    # print(f'ID del servicio: {id(service)}')
    return service.find_all()

@router.get('/{message_id}', response_model=Optional[Message])
def get_message(message_id: int, service: MessageService = Depends(get_message_service)):
    return service.find_by_id(message_id)

@router.get('/details/', response_model=Optional[Message])
def get_message_url_param(message_id: int = Query( ..., ge=1),
                          service: MessageService = Depends(get_message_service)):
    return service.find_by_id(message_id)