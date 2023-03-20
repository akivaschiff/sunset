from astral import LocationInfo
from astral.sun import sun, SunDirection, golden_hour
from datetime import datetime, timedelta

# Define the location (Jerusalem)
city = LocationInfo("Jerusalem", "Israel", "Israel", 31.7683, 35.2137)


def betweener(current_date_time):
    return lambda x, y: x <= current_date_time <= y


def getInterval(current_date_time):
    golden_hour_setting_start, golden_hour_setting_end = golden_hour(city.observer, date = current_date_time.date(),
                                                                     tzinfo = city.timezone,
                                                                     direction = SunDirection.SETTING)
    s = sun(city.observer, date = current_date_time.date(), tzinfo = city.timezone)
    points_in_time = [
        s['dawn'] - timedelta(minutes = 15),
        golden_hour_setting_start - timedelta(minutes = 30),
        golden_hour_setting_end,
        s['dusk'] + timedelta(minutes = 15),
    ]

    intervals = [
        30,
        10,
        20,
    ]
    interval_index = [index for index, times in enumerate(zip(points_in_time[:-1], points_in_time[1:])) if
                      times[0] <= current_date_time <= times[1]]
    if interval_index:
        return intervals[interval_index[0]]
    return 60


if __name__ == '__main__':
    import pytz

    israel_tz = pytz.timezone('Israel')
    israel_tz._utcoffset = timedelta(seconds = 7200)

    print('running intervaler tests')
    assert getInterval(datetime(2023, 3, 14, 18, 0, 0, 0, israel_tz)) == 10
    assert getInterval(datetime(2023, 3, 14, 18, 25, 0, 0, israel_tz)) == 20
    assert getInterval(datetime(2023, 3, 14, 5, 40, 0, 0, israel_tz)) == 30
    assert getInterval(datetime(2023, 3, 14, 0, 30, 0, 0, israel_tz)) == 60

    print('tests pass!')
