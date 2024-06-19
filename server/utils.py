import random


def convert_url(url: str):
    options = [
        "www.naver.com",
        "www.google.com",
        "www.daum.net",
        "www.nate.com",
        "github.com",
    ]
    return random.choice(options)
