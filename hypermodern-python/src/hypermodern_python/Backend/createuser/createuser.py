from fastapi import FastAPI, HTTPException, APIRouter
from app.models import User
from db.supabase import create_supabase_client
import bcrypt
import supabase
import logging

app = FastAPI()
supabase_client = create_supabase_client()

# Configure logging
logging.basicConfig(level=logging.ERROR)


def user_exists(key: str = "email", value: str = None):
    user = supabase_client.from_("user_table").select("*").eq(key, value).execute()
    return len(user.data) > 0

router = APIRouter()
# Create a new user
@router.post("/createuser")
def create_user(user: User):
    try:
        # Convert email to lowercase
        user_email = user.email.lower()
        # Hash password
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

        # Check if user already exists
        if user_exists(value=user_email):
            return {"message": "User already exists"}

        # Add user to users table
        user_data = {
            "name": user.name,
            "email": user_email,
            #"password": hashed_password.decode('utf-8')  # Decode bytes to string
            "password": user.password  # Save plain text password
        }

        user_response = supabase_client.from_("user_table").insert(user_data).execute()
        # Check if user was added
        if user_response:
            return {"message": "User created successfully"}
        else:
            return {"message": "User creation failed"}
    except Exception as e:
        print("Error: ", e)
        return {"message": "User creation failed"}

        