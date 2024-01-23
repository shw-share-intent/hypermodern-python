from fastapi import APIRouter

router = APIRouter()

from . import createuser

router.include_router(createuser.router)