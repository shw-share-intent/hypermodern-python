from fastapi import FastAPI, HTTPException
from app.models import User
from addNotes import router as addNotes_router
from getuser import router as getuser_router
from updateuser import router as updateuser_router
from createuser import router as create_router
from deleteNotes import router as deleteNotes_router
from db.supabase import create_supabase_client
import bcrypt
import supabase
import logging

app = FastAPI()


app.include_router(addNotes_router)
app.include_router(create_router)
app.include_router(getuser_router)
app.include_router(updateuser_router)
app.include_router(deleteNotes_router)


@app.get("/")
def read_item():
    return "Welcome to Share Intent backend"

