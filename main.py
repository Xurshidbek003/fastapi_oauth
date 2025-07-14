from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.auth import login_router
from routers.users import user_router

app = FastAPI(title='Auth', version='1.0', docs_url='/')

app.include_router(user_router)
app.include_router(login_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)







