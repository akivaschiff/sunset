from astral import LocationInfo
from astral.sun import sun, SunDirection, golden_hour
from datetime import datetime, timedelta

# Define the location (Jerusalem)
city = LocationInfo("Jerusalem", "Israel", "Israel", 31.7683, 35.2137)


def betweener(current_date_time):
    return lambda x, y: x <= current_date_time <= y


def getInterval(current_date_time):
    golden_hour_rising_start, golden_hour_rising_end = golden_hour(city.observer, date = current_date_time.date(),
                                                                   tzinfo = city.timezone,
                                                                   direction = SunDirection.RISING)
    golden_hour_setting_start, golden_hour_setting_end = golden_hour(city.observer, date = current_date_time.date(),
                                                                     tzinfo = city.timezone,
                                                                     direction = SunDirection.SETTING)
    s = sun(city.observer, date = current_date_time.date(), tzinfo = city.timezone)

    points_in_time = [
        golden_hour_rising_start,
        golden_hour_rising_end,
        s['noon'] + timedelta(hours = 1),
        golden_hour_setting_start - timedelta(minutes = 45),
        golden_hour_setting_end,
        s['dusk'] + timedelta(minutes = 30),
    ]
    # print(current_date_time)
    # print('===============')
    # for point in points_in_time:
    # 	print(point)

    intervals = [
        30,
        30,
        20,
        10,
        30,
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
    assert getInterval(datetime(2023, 3, 14, 18, 30, 0, 0, israel_tz)) == 30
    assert getInterval(datetime(2023, 3, 14, 5, 40, 0, 0, israel_tz)) == 30
    assert getInterval(datetime(2023, 3, 14, 12, 0, 0, 0, israel_tz)) == 60
    assert getInterval(datetime(2023, 3, 14, 15, 30, 0, 0, israel_tz)) == 30
    assert getInterval(datetime(2023, 3, 14, 0, 30, 0, 0, israel_tz)) == 180

    print('tests pass!')
