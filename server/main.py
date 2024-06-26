import logging
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from .database import engine, SessionLocal
from .models import Base
from .schemas import URLBase, URL
from .services import (
    create_short_url, get_original_url,
    update_stat,
)


log = logging.getLogger(__name__)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# check origin domain
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post(
    "/shorten",
    response_model=URL,
)
def shorten_url(
    url: URLBase,
    db: Session = Depends(get_db)
):
    if url.url == "":
        raise HTTPException(
            status_code=400,
            detail="URL is required",
        )
    return create_short_url(url=url, db=db)


@app.get(
    "/{short_key}",
    response_class=RedirectResponse,
)
def redirect_url(
    short_key: str,
    db: Session = Depends(get_db)
):
    item = update_stat(
        db=db,
        short_url=short_key,
    )
    if item is None:
        raise HTTPException(
            status_code=404,
            detail="URL not found",
        )
    return RedirectResponse(
        url=item.url,
        status_code=status.HTTP_301_MOVED_PERMANENTLY
    )


@app.get(
    "/stats/{short_key}",
)
def get_stats(
    short_key: str,
    db: Session = Depends(get_db)
):
    item = get_original_url(
        db=db,
        short_url=short_key,
    )
    if item is None:
        raise HTTPException(
            status_code=404,
            detail="URL not found",
        )
    return {"stats": item.stats}
