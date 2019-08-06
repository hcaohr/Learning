import aircv as ac
from appium import webdriver
import time
from ImageIdentification.test_aircv import find_coordinate_by_image_identify, click_according_to_coordinate


desired_caps = {
    "appPackage": "com.qiyi.video",
    "appActivity": ".WelcomeActivity",
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Mix3",
    "udid": "bab67515",
    "automationName": "UiAutomator2",
    "noReset": True,
    "newCommandTimeout": 3600,
    "launchTimeout": 6000,
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)

x, y = find_coordinate_by_image_identify(driver, "./image/dianshiju.jpg")
driver.tap([(x, y)])
time.sleep(2)

driver.quit()
