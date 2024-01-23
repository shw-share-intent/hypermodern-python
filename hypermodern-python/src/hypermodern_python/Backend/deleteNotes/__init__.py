from fastapi import APIRouter

router = APIRouter()

from . import deleteNotes

router.include_router(deleteNotes.router)