from fastapi import APIRouter
from typing import List
import api.schemas.user as user_schema

router = APIRouter()


@router.get("/user", response_model=List[user_schema.User])
async def get_userData():
    return user_schema.User(userId=63151, point=100, exchange={}, histories=[user_schema.History(clubId=10, description="初期ポイント", dateTime="0:0:0", point=100)])
@router.put("/user/update")
async def put_userData():
    pass
@router.put("/user/visit")
async def visit():
    pass
@router.post("/user/register")
async def userRegister():
    pass