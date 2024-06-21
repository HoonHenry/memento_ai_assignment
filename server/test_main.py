import datetime as _dt
import logging
import os
# import aioredis
from fastapi.testclient import TestClient

from .main import app


log = logging.getLogger(__name__)

# rd = aioredis.from_url(
#     f"redis://{os.environ.get('REDIS_HOST')}:{os.environ.get('REDIS_PORT')}",
#     decode_responses=True
# )
# log.info(rd)

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_shorten_url():
    response = client.post(
        "/shorten",
        json={"url": "https://www.naver.com"},
    )
    assert response.status_code == 200
    assert "short_url" in response.json()
    assert "valid_by" in response.json()
    assert response.json()["url"] == "https://www.naver.com"


def test_shorten_url_with_null():
    response = client.post(
        "/shorten",
        json={"url": None},
    )
    assert response.status_code == 422


def test_shorten_url_with_empty_string():
    response = client.post(
        "/shorten",
        json={"url": ""},
    )
    assert response.status_code == 400


def test_shorten_url_with_expiration_time():
    due = _dt.datetime.now() + _dt.timedelta(hours=2)
    due = str(due)
    payload = {
        "url": "https://www.naver.com",
        "valid_by": due
    }
    response = client.post(
        "/shorten",
        json=payload,
    )
    log.info(response.json())
    assert response.status_code == 200
    assert "short_url" in response.json()
    assert "valid_by" in response.json()
    assert response.json()["url"] == "https://www.naver.com"
    assert response.json()['valid_by'] == due


def test_shorten_url_with_a_wrong_expiration_time_format():
    due = "240701"
    payload = {
        "url": "https://www.naver.com",
        "valid_by": due
    }
    response = client.post(
        "/shorten",
        json=payload,
    )
    log.info(response.json())
    assert response.status_code == 422


def test_redirect_url():
    response = client.post(
        "/shorten",
        json={"url": "https://www.naver.com"},
    )
    short_key = response.json()["short_url"]
    url = response.json()['url']
    response2 = client.get(
        f"/{short_key}"
    )
    log.info(response2.json())

    assert response2.status_code == 301
    assert response2.json()["url"] == url


def test_redirect_url_not_found():
    response = client.post(
        "/shorten",
        json={"url": "https://www.naver.com"},
    )
    response = client.get(
        "/0000000"
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "URL not found"


def test_get_stats():
    response = client.post(
        "/shorten",
        json={"url": "https://www.naver.com"},
    )
    short_key = response.json()["short_url"]
    response = client.get(
        f"/{short_key}"
    )
    log.info(response.json())
    response = client.get(
        f"/stats/{short_key}"
    )
    log.info(response.json())
    assert response.json()["stats"] == 1
