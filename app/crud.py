from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models import User
from bson import ObjectId

async def create_user(db: AsyncIOMotorDatabase, user: User):
    user_dict = user.dict()
    result = await db.users.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict

async def get_users(db: AsyncIOMotorDatabase):
    users = []
    async for user in db.users.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users

async def get_user(db: AsyncIOMotorDatabase, user_id: str):
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
    return user

async def update_user(db: AsyncIOMotorDatabase, user_id: str, user: User):
    await db.users.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict()})
    return await get_user(db, user_id)

async def delete_user(db: AsyncIOMotorDatabase, user_id: str):
    result = await db.users.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count == 1 