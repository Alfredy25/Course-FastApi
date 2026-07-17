
from pydantic import BaseModel, Field
from enum import Enum

class CoverageType(str, Enum):
    PAQUETEXPRESS = "PAQUETEXPRESS"
    ZONA_PLUS = "ZONA PLUS"
    ZONA_PLUS_ESPECIAL = "ZONA PLUS ESPECIAL"


class CoveragePX(BaseModel):
    id_delivery: int | None = None
    postal_code: str = Field(..., min_length=4, max_length=5,
                             description="clave codigo postal entre 4 y 5 caracteres.")
    township: str = Field(..., min_length=3, max_length=60,
                          description="Colonia o Asentamiento")
    municipality: str = Field(..., min_length=3, max_length=50,
                              description="Delegación o Municipio")
    city: str = Field(..., min_length=3, max_length=60,
                      description="Ciudad")
    state: str = Field(..., min_length=4, max_length=60,
                       description="Estado de la republica Méxicana")
    coverage_type: CoverageType

