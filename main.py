from fastapi import FastAPI

from database.database import engine
from models.models import Base
from routes.router import router

app = FastAPI()
app.include_router(router)

Base.metadata.create_all(engine)


@app.get("/")
def welcome():
    return {"message": "Welcome to my INCOME-EXPENDITURE project!"}
