import datetime as _dt
from sqlalchemy import Column, Integer, String, DateTime

from .database import Base


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
    valid_by = Column(
        DateTime,
        # default=_dt.datetime.now()+_dt.timedelta(hours=1),
        default=_dt.datetime.now()+_dt.timedelta(seconds=30),
    )
    created_at = Column(
        DateTime,
        default=_dt.datetime.now(),
    )
