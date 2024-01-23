from fastapi import FastAPI, HTTPException, APIRouter
from app.models import User
from db.supabase import create_supabase_client
import supabase
import logging

app = FastAPI()
supabase_client = create_supabase_client()

# Configure logging
logging.basicConfig(level=logging.ERROR)

router = APIRouter()

@router.post("/delete")
def delete_user(email: str):
    try:
        # Check if user exists
        user_response = supabase_client.from_("user_table").delete().eq("email", email).execute()

        # Check if user was deleted successfully
        if user_response:
            return "user deleted sucucessfully"
        else:
            return "User deletion failed"
    except Exception as e:
        logging.error("Error: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
