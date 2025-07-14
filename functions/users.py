from models.users import Users
from routers.auth import get_password_hash


def sign_up(form, db):
    user = Users(
        username=form.username,
        password=get_password_hash(form.password)
    )
    db.add(user)
    db.commit()
    return {'message': "Ro'yxatdan muvofaqqiyatli o'tdingiz !"}


def update_user(form, db, current_user):
    db.query(Users).filter(Users.id == current_user.id).update({
        'username': form.username,
        'password': get_password_hash(form.password)
    })
    db.commit()
    return {'message': 'Profil muvofaqqiyatli tahrirlandi !'}
