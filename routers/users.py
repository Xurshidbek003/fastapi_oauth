from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import database
from functions.users import sign_up
from models.users import Users
from schemas.users import SchemaUser

user_router = APIRouter(tags=['Users'], prefix='/users')


@user_router.get('/get')
def get_users(db: Session = Depends(database)):
    try:
        return db.query(Users).all()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@user_router.post('/create')
def royxatdan_otish(form: SchemaUser, db: Session = Depends(database)):
    try:
        return sign_up(form, db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))