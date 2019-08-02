import aircv as ac
from selenium import webdriver
import unittest, time
from selenium.webdriver.common.action_chains import ActionChains


"""
要调用aircv库，如果按照的opencv-contrib-python是最新版本，会报错：
Set OPENCV_ENABLE_NONFREE CMake option and rebuild the library in function 'create'

解决方法：
要先把最新的opencv-contrib-python卸载，然后按照指定版本的：
pip3 install opencv-contrib-python==3.4.2.16

参考链接：
1. https://stackoverflow.com/questions/52305578/sift-cv2-xfeatures2d-sift-create-not-working-even-though-have-contrib-instal
2. https://blog.csdn.net/nima1994/article/details/86133257

"""


def click(self, imgsrc, imgobj):
    imsrc = ac.imread(imgsrc)  # 原始图像
    imsch = ac.imread(imgobj)  # 待查找的部分
    position = ac.find_sift(imsrc, imsch)

    x, y = position['result']

    print("x = ", x)
    print("y = ", y)

    ActionChains(self.driver).move_by_offset(x, y).click().perform()  # 点击操作


class Test01(unittest.TestCase):
    def test_start(self):
        try:
            self.driver = webdriver.Chrome()
            self.driver.get("https://www.baidu.com/")
            self.driver.maximize_window()
            self.driver.save_screenshot("/image/baidu.jpg")

            imgsrc = '/image/baidu.jpg'
            imgobj = '/image/baidu_logo.jpg'
            click(self, imgsrc, imgobj)
            time.sleep(3)

            self.driver.quit()
        except Exception as msg:
            print(msg)


if __name__ == "__main__":
    unittest.main()
