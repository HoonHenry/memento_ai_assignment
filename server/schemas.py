import datetime as _dt
from pydantic import BaseModel


class URLBase(BaseModel):
    url: str


class URLCreate(URLBase):
    pass


class URL(URLBase):
    id: int
    short_url: str
    valid_by: _dt.datetime
    created_at: _dt.datetime

    class Config:
        orm_mode = True
