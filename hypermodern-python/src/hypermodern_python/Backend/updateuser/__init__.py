from fastapi import APIRouter

router = APIRouter()

from . import updateuser

router.include_router(updateuser.router)