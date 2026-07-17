from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from course.alfredo.fastapi.webapi.entities import CoveragePX


class CoveragePXRepository:
    def __init__(self, db: Session):
        self._db = db

    def find_by_cp(self, coverage_cp: str) -> List[CoveragePX]:
        stmt = select(CoveragePX).where(CoveragePX.postal_code == coverage_cp)
        coverages =  self._db.scalars(stmt).all()
        return list(coverages)






