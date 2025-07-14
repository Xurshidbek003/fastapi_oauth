from fastapi import HTTPException
from models.users import Users
from routers.auth import get_password_hash
from utils.send_email import send_email
from random import randrange
from utils.redis_client import r


def sign_up(form, db, background_tasks):

    if db.query(Users).filter(Users.username == form.username).first():
        raise HTTPException(status_code=400, detail="Username band")

    if db.query(Users).filter(Users.email == form.email).first():
        raise HTTPException(status_code=400, detail="Email band")

    verify_code = str(randrange(100000, 999999))
    redis_key = f"verify:{form.email}"
    redis_data = {
        "username": form.username,
        "password": get_password_hash(form.password),
        "code": verify_code
    }

    r.hmset(redis_key, redis_data)
    r.expire(redis_key, 60)

    subject = "Email tasdiqlash"
    message = f"Sizning tasdiqlash kodingiz: {verify_code}"
    background_tasks.add_task(send_email, form.email, subject, message)
    return {'message': "Ro'yxatdan muvofaqqiyatli o'tdingiz !"}


def verify_email(form, db):
    redis_key = f"verify:{form.email}"
    data = r.hgetall(redis_key)

    if not data:
        raise HTTPException(status_code=400, detail="Kod muddati tugagan yoki mavjud emas")

    if data.get("code") != form.code:
        raise HTTPException(status_code=400, detail="Kod noto‘g‘ri")

    user = Users(
        username=data["username"],
        email=form.email,
        password=data["password"]
    )
    db.add(user)
    db.commit()
    r.delete(redis_key)
    return {"message": "Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi"}


def update_user(form, db, current_user):
    db.query(Users).filter(Users.id == current_user.id).update({
        'username': form.username,
        'password': get_password_hash(form.password)
    })
    db.commit()
    return {'message': 'Profil muvofaqqiyatli tahrirlandi !'}
