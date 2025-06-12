from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
from app.models import User
from app.crud import create_user, get_users, get_user, update_user, delete_user
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

MONGODB_URI = os.getenv('MONGODB_URI')
client = AsyncIOMotorClient(MONGODB_URI)
db = client.get_default_database()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def read_root():
    return {"message": "Leaderboard Backend API"}

@app.post('/users')
async def api_create_user(user: User):
    created = await create_user(db, user)
    return created

@app.get('/users')
async def api_get_users():
    return await get_users(db)

@app.get('/users/{user_id}')
async def api_get_user(user_id: str):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put('/users/{user_id}')
async def api_update_user(user_id: str, user: User):
    updated = await update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@app.delete('/users/{user_id}')
async def api_delete_user(user_id: str):
    deleted = await delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": True}
