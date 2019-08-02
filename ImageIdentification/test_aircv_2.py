import aircv as ac
from selenium import webdriver
from ImageIdentification.test_aircv import find_coordinates_by_image_identify, click_according_to_coordinate


driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()

#imsrc = ac.imread("/image/baidu.jpg")  # 原始图像
#imsch = ac.imread("/image/lantern_icon.jpg")  # 待查找的部分，查找不到的图片
#imsch = ac.imread("./image/baidu_logo.jpg")  # 待查找的部分，可以查找到的图片
cor = find_coordinates_by_image_identify(driver, "./image/baidu_logo.jpg")
print(cor)
click_according_to_coordinate(driver, cor[0][0], cor[0][1])

driver.quit()