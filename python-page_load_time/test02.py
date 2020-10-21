from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

''' Create a Chrome webdriver instance'''
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

''' Open the webpage under test'''
driver.get('http://lambdatest.com')
timeout = 5

''''' Test case 1 - The required div-id is not present on the web-page '''''
# while True:
try:
    element_present = EC.presence_of_element_located((By.ID, 'owl-example-1'))
    WebDriverWait(driver, timeout).until(element_present)
    print("1 - Element is present on the page")
#        break
except TimeoutException as ex:
    print("1 - Timed out waiting for page to load " + str(ex))
#        break

''''' Test case 2 - The required div-id is not present on the web-page '''''
# while True:
try:
    element_present = EC.presence_of_element_located((By.ID, 'owl-example'))
    WebDriverWait(driver, timeout).until(element_present)
    print("2 - Element is present on the page")
#        break
except TimeoutException as ex:
    print("2 - Timed out waiting for page to load " + str(ex))
#        break

''' Free up the resources'''
driver.close()
driver.quit()