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
        json={"url": "https://www.example.com"},
    )
    assert response.status_code == 200
    assert "short_url" in response.json()


def test_redirect_url():
    response = client.post(
        "/shorten",
        json={"url": "https://www.example.com"},
    )
    short_key = response.json()["short_url"]
    response2 = client.get(
        f"/{short_key}"
    )
    log.info(response2.json())

    # assert response2.json()["url"] == "https://www.example.com" == 301
    # assert response2.json()["stats"] > 0


def test_redirect_url_not_found():
    response = client.post(
        "/shorten",
        json={"url": "https://www.example.com"},
    )
    response = client.get(
        f"/123567890"
    )
    assert response.status_code == 404
    # assert response2.json()["detail"] == "URL not found"


def test_get_stats():
    response = client.post(
        "/shorten",
        json={"url": "https://www.example.com"},
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
