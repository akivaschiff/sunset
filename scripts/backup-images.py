import os
import sys
import shutil
import glob
from datetime import timedelta, datetime

image_folder = './images'
backup_folder = '/media/akiva/Elements/sunset-images'

def backup_yesterday(current_date):
    date_prefix = (current_date - timedelta(days = 1)).strftime("%Y-%m-%d")
    directory = os.path.join(backup_folder, date_prefix)
    if not os.path.exists(directory):
        os.makedirs(directory)

    files_to_move = glob.glob(os.path.join(image_folder, f'image_{date_prefix}*'))
    for file_path in files_to_move:
        shutil.move(file_path, directory)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        backup_yesterday(datetime.strptime(sys.argv[1], '%Y-%m-%d'))
    else:
        backup_yesterday(datetime.now())