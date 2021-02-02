from selenium import webdriver


class Browser:
    def __init__(self, driver=None):
        self.driver = driver

    def get_page_load_time(self):
        """
        refer to: https://www.lambdatest.com/blog/how-to-measure-page-load-times-with-selenium/
        :return:
        """
        # Use Navigation Timing  API to calculate the timings that matter the most
        navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")

        # Calculate the performance
        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        print("Back End: %s" % backendPerformance_calc)
        print("Front End: %s" % frontendPerformance_calc)

        return backendPerformance_calc, frontendPerformance_calc


if __name__ == '__main__':
    hyperlink = "http://lambdatest.com"
    driver = webdriver.Chrome()
    driver.get(hyperlink)

    Browser(driver=driver).get_page_load_time()
    driver.quit()
