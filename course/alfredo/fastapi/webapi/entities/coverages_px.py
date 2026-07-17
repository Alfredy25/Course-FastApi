from course.alfredo.fastapi.webapi.config.db import Base
from enum import Enum as PyEnum
from sqlalchemy import String, Enum, Index
from sqlalchemy.orm import Mapped, mapped_column


class CoverageType(str, PyEnum):
    PAQUETEXPRESS = "PAQUETEXPRESS"
    ZONA_PLUS = "ZONA PLUS"
    ZONA_PLUS_ESPECIAL = "ZONA PLUS ESPECIAL"

class CoveragePX(Base):
    __tablename__ = "coverages_px"

    id_delivery: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    branch: Mapped[str | None] = mapped_column(String(50)) # Sucursal
    place: Mapped[str | None] = mapped_column(String(30)) # Plaza
    postal_code: Mapped[str] = mapped_column(String(10), nullable=False)
    township: Mapped[str] = mapped_column(String(100), nullable=False)
    municipality: Mapped[str] = mapped_column(String(150), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str] = mapped_column(String(100), nullable=False)

    coverage_type: Mapped[CoverageType] = mapped_column(Enum(CoverageType), nullable=False)

    __table_args__ = (Index("idx_postal_code", "postal_code"))


