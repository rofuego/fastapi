from sqlalchemy.orm import Session
from model import Post
from schema import PostRequest


def get_all_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()


def save_post(db: Session, post: PostRequest):
    _post = Post(title=post.title, body=post.body)
    db.add(_post)
    db.commit()
    db.refresh(_post)
    return _post
