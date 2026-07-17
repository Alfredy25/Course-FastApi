"""
En FastAPI, estos modelos Pydantic suelen usarse como:
    * DTOs de entrada.
    * DTOs de salida.
    * Esquemas de validación.
    * Contratos de la API.
Un DTO es un objeto con datos.
"""

from pydantic import BaseModel, Field, EmailStr


class Message(BaseModel):
    id: int | None = None
    text: str = Field(...,
                      min_length=8,
                      max_length=50,
                      description="Contenido del mensaje entre 8 y 50 caracteres.")
    author_email: EmailStr | None = Field(
        default=None,
        description="Email del autor es opcional pero debe de tener un formato valido si se envia"
    )
    priority: int = Field(default=1, ge=1, le=5, description="Priority del mensaje entre 1 (baja) y 5 (alta).")
