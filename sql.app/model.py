from database import Base
from sqlalchemy import Column, Integer, String


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
