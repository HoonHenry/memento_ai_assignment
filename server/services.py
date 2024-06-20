import datetime as _dt

from . import models, schemas
from .utils import convert_url, set_timedelta
from sqlalchemy.orm import Session


def get_original_url(
    db: Session,
    short_url: str,
):
    return db.query(models.URL).filter(
        models.URL.short_url == short_url
    ).first()


def get_url_stats(
    db: Session,
    short_url: str,
):
    item = db.query(models.URL).filter(
        models.URL.short_url == short_url
    ).first()
    if item.valid_by < _dt.datetime.utc:
        update_stat(db, item)
    return item


def update_valid_time(
    db: Session,
    item: schemas.URL,
):
    item.valid_by = _dt.datetime.now() + set_timedelta()
    db.commit()
    db.refresh(item)
    return item


def update_stat(
    db: Session,
    short_url: str,
):
    item = get_url_stats(
        db=db,
        short_url=short_url,
    )
    if item is None:
        return None
    item.stats += 1
    db.commit()
    db.refresh(item)
    return item


def create_short_url(
    db: Session,
    url: schemas.URLCreate,
):
    instance = models.URL(
        url = url.url,
        short_url = convert_url(),
        valid_by = url.valid_by
    )
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
