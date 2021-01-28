import wave
import pyaudio
import cv2
import time
import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

# ================ audio setting =================
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
WAVE_OUTPUT_FILENAME = PATH("output.wav")

p = pyaudio.PyAudio()
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)

audio_record_flag = True


def callback(in_data, frame_count, time_info, status):
    wf.writeframes(in_data)
    if audio_record_flag:
        return (in_data, pyaudio.paContinue)
    else:
        return (in_data, pyaudio.paComplete)


stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                input=True,
                stream_callback=callback)

# ================ video setting =================
width = 640
height = 480
video_name = PATH('test.avi')
cap = cv2.VideoCapture(0)  # 默认的摄像头
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 编码格式
# 经实际测试，单线程下最高帧率为10帧/秒，且会变动，因此选择9.5帧/秒
# 若设置帧率与实际帧率不一致，会导致视频时间与音频时间不一致

print("video recording...")
print("audio recording...")

first_time = True
while cap.isOpened():
    stream.start_stream()
    if first_time:
        video = cv2.VideoWriter(video_name, fourcc, 30, (width, height))
        first_time = False
    ret, frame = cap.read()
    # frame = RotateClockWise180(frame)
    if ret:
        video.write(frame)
        #
        cv2.imshow('frame', frame)
        # 等待按键q操作关闭摄像头
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# stop audio
print("stop audio")
audio_record_flag = False
while stream.is_active():
    time.sleep(0.25)
stream.stop_stream()
stream.close()
wf.close()
p.terminate()

# stop video
print("stop video")
video.release()
cap.release()
cv2.destroyAllWindows()

print("merge video & audio")
merge_video = PATH('merge.mp4')
cmd = 'ffmpeg -i {} -i {} -c:v copy -c:a aac -strict experimental {}'.format(video_name, WAVE_OUTPUT_FILENAME, merge_video)
print(cmd)
# os.popen(cmd)
