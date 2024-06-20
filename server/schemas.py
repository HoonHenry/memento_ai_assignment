from typing import Optional
import datetime as _dt
from pydantic import BaseModel


class URLBase(BaseModel):
    url: str
    valid_by: _dt.datetime | None = None


class URLCreate(URLBase):
    pass


class URL(URLBase):
    id: int
    short_url: str
    stats: int
    created_at: _dt.datetime

    class Config:
        orm_mode = True
