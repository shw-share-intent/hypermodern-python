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

def user_exists(key: str = "email", value: str = None):
    user = supabase_client.from_("user_table").select("*").eq(key, value).execute()
    return len(user.data) > 0

# Create a new user
@router.post("/updateuser")
def update_user(user: User):
    try:
        # Check if user exists
        if user_exists("email", user.email):
            # Update user
            user_data = {"name": user.name, "password": user.password}
            updated_user = supabase_client.from_("user_table").update(user_data).eq("email", user.email).execute()

            if updated_user:
                return {"message": "User updated successfully"}
            else:
                return {"message": "User update failed"}
        else:
            return {"message": "User does not exist"}
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "User update failed"}
