from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timedelta
import pytz

israel_tz = pytz.timezone('Israel')
israel_tz._utcoffset = timedelta(seconds = 7200)

# Define the location (Jerusalem)
city = LocationInfo("Jerusalem", "Israel", "Israel", 31.7683, 35.2137)

def image_name_to_date(image_name):
    date = datetime.strptime(image_name[-23:-4], '%Y-%m-%d_%H-%M-%S')
    return israel_tz.localize(date)

def choose_timelapse_images(image_files, current_date_time):
    s = sun(city.observer, date = current_date_time.date(), tzinfo = city.timezone)
    timelapse_start = s['sunset'] - timedelta(hours = 3)
    timelapse_end = s['dusk'] + timedelta(minutes = 15)
    return [image_file for image_file in image_files if timelapse_start < image_name_to_date(image_file) < timelapse_end]

if __name__ == '__main__':
    image_files = [
        'image_2023-03-12_00-30-00.jpg',
        'image_2023-03-12_11-11-00.jpg',
        'image_2023-03-12_17-00-00.jpg',
        'image_2023-03-12_18-00-00.jpg',
        'image_2023-03-12_19-00-00.jpg',
    ]
    assert len(choose_timelapse_images(image_files, datetime(2023, 3, 12, 21, 0, 0, 0, israel_tz))) == 2
