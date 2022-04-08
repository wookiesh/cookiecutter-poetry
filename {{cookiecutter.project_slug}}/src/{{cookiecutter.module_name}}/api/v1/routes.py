"""Routes for the V1 api."""

import logging

from fastapi import APIRouter
from rollbar.contrib.fastapi import add_to

logger = logging.getLogger(__name__)

router = APIRouter()
add_to(router)


@router.get("/")
async def get_root() -> None:
    """First endpoint."""
    return {"status": "ok"}
