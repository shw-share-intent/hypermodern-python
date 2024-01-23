from fastapi import APIRouter

router = APIRouter()

from . import addNotes

router.include_router(addNotes.router)