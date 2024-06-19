from . import models, schemas
from .utils import convert_url
from sqlalchemy.orm import Session


def get_original_url(
    db: Session,
    short_url: str,
):
    return db.query(models.URL).filter(
        models.URL.short_url == short_url
    ).first()


def create_short_url(
    db: Session,
    url: schemas.URLCreate,
):
    instance = models.URL(
        url = url.url,
        short_url = convert_url(url)
    )
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
