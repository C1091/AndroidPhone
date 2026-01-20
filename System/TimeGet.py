# TimeGet.py
# Location-aware time utility module

import time
from datetime import datetime, timezone

# Try to get local timezone (best method)
try:
    from tzlocal import get_localzone
    LOCAL_TZ = get_localzone()
except Exception:
    LOCAL_TZ = None


def now():
    """
    Returns current local datetime (location-based if possible)
    """
    if LOCAL_TZ:
        return datetime.now(LOCAL_TZ)
    return datetime.now()


def utc_now():
    """
    Returns current UTC datetime
    """
    return datetime.now(timezone.utc)


def timestamp():
    """
    Returns current Unix timestamp (seconds)
    """
    return int(time.time())


def timestamp_ms():
    """
    Returns current Unix timestamp (milliseconds)
    """
    return int(time.time() * 1000)


def date_string(format="%Y-%m-%d"):
    """
    Returns local date string
    """
    return now().strftime(format)


def time_string(format="%H:%M:%S"):
    """
    Returns local time string
    """
    return now().strftime(format)


def datetime_string(format="%Y-%m-%d %H:%M:%S"):
    """
    Returns local date & time string
    """
    return now().strftime(format)


def timezone_name():
    """
    Returns detected timezone name
    """
    if LOCAL_TZ:
        return str(LOCAL_TZ)
    return time.tzname[0]


def sleep(seconds: float):
    """
    Sleep for given seconds
    """
    time.sleep(seconds)


# Test run
if __name__ == "__main__":
    print("Local datetime:", now())
    print("UTC datetime:", utc_now())
    print("Timezone:", timezone_name())
    print("Timestamp:", timestamp())
    print("Timestamp (ms):", timestamp_ms())
