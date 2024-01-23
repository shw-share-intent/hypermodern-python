from fastapi import APIRouter, HTTPException



router = APIRouter()

@router.post("/addnotes")
def add(data):
        
        print("Note is : ",data)
        return "Thank you for your Response your input is stored"
   
