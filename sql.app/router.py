from fastapi import APIRouter, Depends
from database import SessionLocal
from sqlalchemy.orm import Session
from schema import PostRequest
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("", status_code=200)
async def get_all_posts(db: Session = Depends(get_db)):
    _posts = crud.get_all_posts(db, 0, 100)
    return _posts


@router.post("", status_code=201)
async def save_post(request: PostRequest, db: Session = Depends(get_db)):
    _post = crud.save_post(db, request)
    return _post
