import threading
import time
import wave

import cv2
import numpy as np
import pyaudio
from colorthief import ColorThief


def video_record(video_path, record_time=10):
    """
    调用摄像头录视频，需要手动按q停止录制
    :return:
    """
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    size = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(video_path, fourcc, 20.0, size)

    start_time = time.time()
    while True:
        _, frame = cap.read()
        # cv2.imshow('Recording...', frame)
        out.write(frame)
        end_time = time.time()
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        if end_time - start_time >= record_time-1:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def image_capture(pic_path):
    """
    截取单帧图片
    :param pic_path:
    :return:
    """
    cap = cv2.VideoCapture(0)
    retval, frame = cap.read()
    cv2.imwrite(pic_path, frame)


def get_rgb(pic_path):
    """
    返回指定图片主要色的RGB值
    :param pic_path:
    :return:
    """
    color_thief = ColorThief(pic_path)
    dominant_rgb = color_thief.get_color(quality=1)
    print(dominant_rgb)


if __name__ == '__main__':
    path = 'out/pic.png'
    vid_path = 'out/vid.mp4'
    video_record(vid_path)
    # image_capture(path)
    # get_dominant_color(path)