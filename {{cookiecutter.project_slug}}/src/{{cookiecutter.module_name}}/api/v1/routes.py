"""Routes for the V1 api."""

import logging

from fastapi import APIRouter
from rollbar.contrib.fastapi import add_to

logger = logging.getLogger(__name__)

router = APIRouter()
add_to(router)


@router.get("/", response_model=dict)
async def get_root() -> dict:
    """First endpoint."""
    return {"status": "ok"}
