# refer to: https://www.jb51.net/article/163992.htm

import pyaudio
import wave
from tqdm import tqdm


def record_audio(save_path, record_time=5):
    """
    调用麦克风录音
    :param save_path: 音频.wav保存路径
    :param record_time: 录制时长
    :return:
    """
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    wf = wave.open(save_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    print("* recording")
    for i in tqdm(range(0, int(RATE / CHUNK * record_time))):
        data = stream.read(CHUNK)
        wf.writeframes(data)
    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()


if __name__ == '__main__':
    sound_path = "sound.wav"
    record_audio("output.wav")
