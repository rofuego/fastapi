from database import Base
from sqlalchemy import Column, Integer, String


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)

