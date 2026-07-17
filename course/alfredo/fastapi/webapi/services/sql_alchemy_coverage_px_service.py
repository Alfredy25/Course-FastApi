from typing import List

from sqlalchemy.orm import Session

from course.alfredo.fastapi.webapi.entities import CoveragePX as CoveragePxEntity
from course.alfredo.fastapi.webapi.models.coverage_px import CoveragePX as CoveragePxDto

from course.alfredo.fastapi.webapi.repositories.sql_alchemy_coverage_repository import CoveragePXRepository
from course.alfredo.fastapi.webapi.services.coverage_service import CoverageService

def entity_to_dto(entity: CoveragePxEntity) -> CoveragePxDto:
    return CoveragePxDto.model_validate({
        'id_delivery': entity.id_delivery,
        'postal_code': entity.postal_code,
        'township': entity.township,
        'municipality': entity.municipality,
        'city': entity.city,
        'state': entity.state,
        'coverage_type': entity.coverage_type,
    })


class SQLAlchemyCoveragePxService(CoverageService):
    def __init__(self, repo: CoveragePXRepository, db: Session):
        self.repo = repo
        self._db = db

    def find_by_cp(self, postal_code: str) -> List[CoveragePxDto]:
        coverages = self.repo.find_by_cp(postal_code)
        if not coverages:
            return []

        return [entity_to_dto(coverage_px) for coverage_px in coverages]
