from pydantic import BaseModel
from typing import Optional


class PostResponse(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    body: Optional[str] = None

    class Config():
        orm_mode = True


class PostRequest(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None

class ErrorResponse(BaseModel):
    code: str
    status: str
    message: str
    path: str
