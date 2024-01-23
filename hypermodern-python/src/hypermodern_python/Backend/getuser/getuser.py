from fastapi import FastAPI, HTTPException, APIRouter
from app.models import User
from db.supabase import create_supabase_client
import supabase
import logging
from typing import Union

app = FastAPI()
supabase_client = create_supabase_client()

# Configure logging
logging.basicConfig(level=logging.ERROR)

router = APIRouter()

def user_exists(key: str = "email", value: str = None):
    user = supabase_client.from_("user_table").select("*").eq(key, value).execute()
    return len(user.data) > 0

@router.post("/getuser")
def get_user(email: str):
    try:
        print(email)
        if email:
            user = supabase_client.from_("user_table")\
                .select("name", "email", "password")\
                .eq("email", email)\
                .execute()
            print(type(user.data))
            if user:
                if user.data:
                    return user.data[0]
                else:
                    return {"message": "User not found"}
        else:
            users = supabase_client.from_("user_table")\
                .select("password", "email", "name")\
                .execute()

            if users and 'data' in users:
                if users['data']:
                    return users['data']
                else:
                    return {"message": "No users found"}
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Internal Server Error"}
