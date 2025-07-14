from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from db import database
from functions.users import sign_up, update_user, verify_email
from routers.auth import get_current_user
from schemas.users import SchemaUser, EmailVerify

user_router = APIRouter(tags=['Users'], prefix='/users')


@user_router.get('/get')
def get_users(current_user: SchemaUser = Depends(get_current_user)):
    try:
        return current_user
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@user_router.post('/create')
def royxatdan_otish(form: SchemaUser, background_tasks: BackgroundTasks, db: Session = Depends(database)):
    try:
        return sign_up(form, db, background_tasks)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@user_router.post("/verify")
def verify_endpoint(form: EmailVerify, db: Session = Depends(database)):
    return verify_email(form, db)

@user_router.put('/update')
def profilni_tahrirlash(form: SchemaUser, db: Session = Depends(database),
                        current_user: SchemaUser = Depends(get_current_user)):
    try:
        return update_user(form, db, current_user)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
