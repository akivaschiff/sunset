import cv2
import os
import sys


def create_video(image_filenames, video_file_name):
    # open the first image to get the image size
    img = cv2.imread(image_filenames[0])
    height, width, channels = img.shape

    # create a video writer object with the specified frame rate and size
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # specify the codec for the output video
    # the web uses a different codec: we will convert later because not sure how here
    temp_video_file_name = f'{video_file_name}.other-codec.mp4'
    out = cv2.VideoWriter(temp_video_file_name, fourcc, 30.0, (width, height))

    # loop through each image in the folder and write it to the video
    for image_filename in image_filenames:
        img = cv2.imread(image_filename)
        out.write(img)

    # release the video writer and close all windows
    out.release()
    cv2.destroyAllWindows()

    # convert codec
    os.system(f"ffmpeg -i {temp_video_file_name} -vcodec libx264 {video_file_name}")
    os.remove(temp_video_file_name)


if __name__ == '__main__':
    pass
