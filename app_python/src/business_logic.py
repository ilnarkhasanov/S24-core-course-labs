from datetime import datetime

import pytz


def get_current_moscow_time() -> datetime:
    moscow_tz = pytz.timezone("Europe/Moscow")
    return moscow_tz.localize(datetime.now())


def get_human_readable_time(dt: datetime) -> str:
    human_readable = dt.strftime("%a, %b %d %Y, %H:%M:%S")
    return human_readable
