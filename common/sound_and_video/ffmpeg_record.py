import os
import signal
import subprocess
import time
import shlex
import cv2
import platform


class Recorder:
    def __init__(self, v_device=None, a_device=None, device_index=None, video_size=None):
        # self.PLATFORM = CONST.PLATFORM
        # self.V_DEVICE = v_device or CONST.VIDEO_DEVICE  # for windows
        # self.A_DEVICE = a_device or CONST.AUDIO_DEVICE  # for windows
        self.PLATFORM = platform.system().lower()
        self.V_DEVICE = v_device or 'Logitech HD Webcam C525'  # for windows
        self.A_DEVICE = a_device or 'Microphone (HD Webcam C525)'  # for windows

        self.DEVICE_INDEX = device_index or '0:1'  # for mac
        self.VIDEO_SIZE = video_size or '1280x720'  # for mac/linux
        self.DISABLE_LOG_FLAG = '-loglevel quiet'

        self.record_process = None

        self.kill_process()

    def kill_process(self):
        if self.PLATFORM == 'windows':
            os.popen('taskkill /f /im ffmpeg.exe')
        elif self.PLATFORM == 'darwin':
            os.popen('killall -2 ffmpeg')
        time.sleep(1)

    def start_recording(self, file_path, framerate=30):
        """
        用ffmpeg直接录制视频+音频
        :param file_path: 视频保存路径
        :return: subprocess子进程对象
        """
        if os.path.exists(file_path):
            os.remove(file_path)
        if self.PLATFORM == 'windows':
            command = f'ffmpeg -f dshow -i video="{self.V_DEVICE}":audio="{self.A_DEVICE}"' \
                      f' {file_path} {self.DISABLE_LOG_FLAG}'
        elif self.PLATFORM == 'darwin':
            command = f'ffmpeg -f avfoundation -s {self.VIDEO_SIZE} -r {framerate} -i "{self.DEVICE_INDEX}" {file_path} {self.DISABLE_LOG_FLAG}'
        else:
            command = f'ffmpeg -f v4l2 -r 30 -s {self.VIDEO_SIZE} -i {self.V_DEVICE} {file_path} {self.DISABLE_LOG_FLAG}'
        # self.record_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        self.record_process = subprocess.Popen(shlex.split(command), shell=False, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        time.sleep(3)
        return self.record_process

    def stop_recording(self):
        if self.record_process:
            print('stopping record')
            if self.PLATFORM == 'windows':
                self.record_process.stdin.write('q'.encode('utf-8'))
                self.record_process.communicate()
            elif self.PLATFORM == 'darwin':
                self.record_process.send_signal(signal.SIGUSR2)
            time.sleep(2)
            # self.record_process.kill()

    @staticmethod
    def take_photo(pic_path):
        """
        截取单帧图片
        :param pic_path:
        :return:
        """
        cap = cv2.VideoCapture(0)
        if os.path.exists(pic_path):
            os.remove(pic_path)
        if cap.isOpened():
            retval, frame = cap.read()
            cv2.imwrite(pic_path, frame)
            time.sleep(1)
            cap.release()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    save_path = './out/out.mp4'
    pic_path = './out/pic.png'
    pic_path2 = './out/pic2.png'
    recorder = Recorder()
    recorder.start_recording(save_path)
    print('hhhh')
    time.sleep(5)
    recorder.stop_recording()
    time.sleep(5)

    recorder.take_photo(pic_path)
    time.sleep(2)
    recorder.take_photo(pic_path2)