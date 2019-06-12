# coding=utf-8
import time
import webcolors
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(6)
driver.get("https://www.baidu.com/")
time.sleep(1)
search_btn = driver.find_element_by_id('setf')
color = search_btn.value_of_css_property('color')
size = search_btn.value_of_css_property('font-size')
print(color)
print(webcolors.rgb_to_name((153, 153, 153)))
driver.quit()