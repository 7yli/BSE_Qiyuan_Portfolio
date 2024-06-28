import time
import threading
from picamera2 import Picamera2

class Camera(object):
    _instance = None  # 单例对象实例
    thread = None  # 背景线程，用于从摄像头读取帧
    frame = None  # 当前帧存储在此
    last_access = 0  # 最后一次客户端访问摄像头的时间
    picam2 = None  # picamera2 实例

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Camera, cls).__new__(cls)
            cls.picam2 = Picamera2()
            capture_config = cls.picam2.create_still_configuration()
            capture_config["main"]["size"] = (320, 240)
            cls.picam2.configure(capture_config)
        return cls._instance

    def __init__(self):
        if not self.thread:
            # 启动后台帧线程
            self.thread = threading.Thread(target=self._thread)
            self.thread.start()

    def get_frame(self):
        Camera.last_access = time.time()
        # 初始化摄像头并等待帧变得可用
        if self.frame is None:
            while self.frame is None:
                time.sleep(0)
        return self.frame

    @classmethod
    def _thread(cls):
        cls.picam2.start()
        try:
            while True:
                # 捕获帧
                cls.frame = cls.picam2.capture_array()
                # 如果在过去10秒内没有客户端请求帧，停止线程
                if time.time() - cls.last_access > 10:
                    break
        finally:
            cls.picam2.stop()
            cls.picam2.close()
            cls.thread = None
            cls.frame = None

# 其他系统部分将像以前一样与Camera类交互
