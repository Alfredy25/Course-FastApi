from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException, status

from course.alfredo.fastapi.webapi.dependencies.message_dependencies import get_coverage_service
from course.alfredo.fastapi.webapi.models.coverage_px import CoveragePX
from course.alfredo.fastapi.webapi.services.coverage_service import CoverageService

router = APIRouter()


@router.get("/", response_model=List[CoveragePX])
def lis_coverages_by_cp(postal_code: str = Query(..., alias="cp"),
        service: CoverageService = Depends(get_coverage_service)):

    coverages = service.find_by_cp(postal_code)
    if not coverages:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"no hay cobertura con el cp {postal_code} en el sistema"
            )
    return coverages
