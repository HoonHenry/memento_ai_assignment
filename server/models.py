import datetime as _dt
from sqlalchemy import Column, Integer, String, DateTime

from .database import Base
from .utils import set_timedelta


class URL(Base):
    __tablename__ = "urls"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    url = Column(
        String,
        index=True,
    )
    short_url = Column(
        String,
        index=True,
        unique=True,
    )
    stats = Column(
        Integer,
        default=0,
    )
    valid_by = Column(
        DateTime,
        default=_dt.datetime.now()+set_timedelta(),
    )
    created_at = Column(
        DateTime,
        default=_dt.datetime.now(),
    )
