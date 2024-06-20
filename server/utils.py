import os
import datetime as _dt
from tsidpy import TSID, TSIDGenerator


def convert_url() -> str:
    datacenter: int = 1
    worker: int = 1
    node: int = datacenter << 5 | worker
    epoch: _dt.datetime = _dt.datetime.fromisoformat(
        '2010-11-04T01:42:54.657Z')

    twitter_generator: TSIDGenerator = TSIDGenerator(
        node=node,
        node_bits=10,
        epoch=epoch.timestamp() * 1000,
        random_fn=lambda n: 0
    )

    tsid: TSID = twitter_generator.create().to_string()
    return tsid


def set_timedelta() -> _dt.datetime:
    timedelta = int(os.environ.get('TIMEDELTA'))  # seconds
    if timedelta == 30:
        timedelta = _dt.timedelta(seconds=30)
    elif timedelta == 3600:
        timedelta = _dt.timedelta(hours=1)
    else:
        raise ValueError('Invalid TIMEDELTA value')

    return timedelta
