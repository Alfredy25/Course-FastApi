"""
Un service representa una capa donde colocas la lógica de aplicación o lógica de negocio.
Un Service es un componente con comportamiento/lógica.
Service = lógica / acciones / casos de uso

Por ejemplo, el service podría encargarse de:
    - Buscar mensaje por ID.

"""
from abc import ABC, abstractmethod
from typing import List, Optional
from course.alfredo.fastapi.webapi.models.coverage_px import CoveragePX as CoveragePxDto


class CoverageService(ABC):

    @abstractmethod
    def find_by_cp(self, postal_code: str) -> List[CoveragePxDto]:
        ...