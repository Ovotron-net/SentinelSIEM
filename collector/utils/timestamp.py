import random
from datetime import datetime, timezone, timedelta


def get_current_utc_timestamp():
    current_time = datetime.now(timezone.utc)
    return iso8601_formatting(current_time)


def iso8601_formatting(timestamp):
    iso_string = timestamp.isoformat().replace("+00:00", "Z")
    return iso_string


# This function generates a single timestamp
def generate_random_timestamp(start_time, end_time):
    if start_time >= end_time:
        raise ValueError("start_time must be before end_time")

    time_difference = end_time - start_time
    total_seconds = int(time_difference.total_seconds())
    random_seconds = random.randint(0, total_seconds)
    new_time = start_time + timedelta(seconds=random_seconds)
    return new_time


# This function will create a list of desired number of timestamps
def random_timestamps(start_time, end_time, num_of_timestamps):
    timestamps = []

    for _ in range(num_of_timestamps):
        timestamps.append(
            iso8601_formatting(
                generate_random_timestamp(start_time, end_time)
            )
        )

    return timestamps


if __name__ == "__main__":
    start = datetime(2026, 7, 1, 10, 0, 0, tzinfo=timezone.utc)
    end = datetime(2026, 7, 1, 12, 0, 0, tzinfo=timezone.utc)

    print(random_timestamps(start, end, 10))
