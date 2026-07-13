"""
En FastAPI, estos modelos Pydantic suelen usarse como:
    * DTOs de entrada.
    * DTOs de salida.
    * Esquemas de validación.
    * Contratos de la API.
Un DTO es un objeto con datos.
"""

from pydantic import BaseModel

class Message(BaseModel):
    id: int
    text: str