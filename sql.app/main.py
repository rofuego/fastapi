from fastapi import FastAPI
import model
from database import engine
import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def welcome():
    return "Welcome"


app.include_router(router.router, prefix="/posts", tags=["posts"])
