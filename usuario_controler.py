from typing import List
from fastapi import APIRouter, Depends, Form, HTTPException
from models import Usuario
from security import criar_token_jwt, verify_password

router = APIRouter()


@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = await Usuario.objects.get_or_none(email=username)
    if not user or not verify_password(password, user.hash_password):
        raise HTTPException(
            status_code=403, detail="Email ou nome de usuário incorretos"
        )
    return {
        "access_token": criar_token_jwt(user.id),
        "token_type": "bearer",
    }
