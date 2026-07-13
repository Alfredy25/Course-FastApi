"""
Un service representa una capa donde colocas la lógica de aplicación o lógica de negocio.
Un Service es un componente con comportamiento/lógica.
Service = lógica / acciones / casos de uso

Por ejemplo, el service podría encargarse de:
    - Listar mensajes.
    - Buscar mensaje por ID.
    - Crear mensaje.
    - Validar reglas.
    - Coordinar repositorios.
    - Llamar otras APIs.
    - Hacer operaciones transaccionales.
    - Unir datos de varias fuentes.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from course.alfredo.fastapi.webapi.models.message import Message


class MessageService(ABC):
    @abstractmethod
    def find_all(self) -> List[Message]:
        ...

    @abstractmethod
    def find_by_id(self, message_id: int) -> Optional[Message]:
        ...
