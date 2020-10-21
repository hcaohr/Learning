
# Loosely based on the example code in http://www.obeythetestinggoat.com/
# how-to-get-selenium-to-wait-for-page-load-after-a-click.html
# Import the necessary packages required for execution

from selenium import webdriver

hyperlink = "http://lambdatest.com"
driver = webdriver.Chrome()
driver.get(hyperlink)

# Use Navigation Timing  API to calculate the timings that matter the most
navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

# Calculate the performance
backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart
print("Back End: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)
driver.quit()