from fastapi import APIRouter

router = APIRouter()

from . import getuser

router.include_router(getuser.router)