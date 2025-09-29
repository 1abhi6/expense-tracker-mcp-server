from fastapi import FastAPI
from app.routers import test 

app = FastAPI()

app.include_router(test.router, prefix="/test", tags=["Test"])
