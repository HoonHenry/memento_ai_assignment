import datetime as _dt

from . import models, schemas
from .utils import convert_url, set_timedelta
from sqlalchemy.orm import Session


def get_original_url(
    db: Session,
    short_url: str,
):
    item = db.query(models.URL).filter(
        models.URL.short_url == short_url
    ).first()
    return item


def update_stat(
    db: Session,
    short_url: str,
):
    item = get_original_url(
        db=db,
        short_url=short_url,
    )
    if item is None:
        return None

    if item.valid_by <= _dt.datetime.now():
        item.valid_by = _dt.datetime.now() + set_timedelta()
        item.short_url = convert_url()
        db.commit()
        db.refresh(item)

    item.stats += 1
    db.commit()
    db.refresh(item)
    return item


def create_short_url(
    db: Session,
    url: schemas.URLCreate,
):
    instance = models.URL(
        url=url.url,
        short_url=convert_url(),
        valid_by=url.valid_by
    )
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
