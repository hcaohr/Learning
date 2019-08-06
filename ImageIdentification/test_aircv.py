import aircv as ac
from selenium.webdriver.common.action_chains import ActionChains


def find_coordinate_by_image_identify(driver, imgsch):
    """
    通过图像识别来查找待查找图片的坐标
    :param driver:
    :param imgsch: 待查找图片
    :return: x, y轴坐标
    """
    try:
        driver.save_screenshot('./image/template.png')
        imsrc = ac.imread('./image/template.png')  # 原始图像
        imsch = ac.imread(imgsch)  # 待查找的部分

        position = ac.find_template(imsrc, imsch)
        if position is not None:
            x, y = position['result']
        else:
            raise Exception("Cannot find the image that you provided.")
        return x, y
    except Exception as msg:
        print(msg)


def find_coordinates_by_image_identify(driver, imgsch):
    """
    通过图像识别来查找全部符合条件的待查找图片的坐标
    :param driver:
    :param imgsch: 待查找图片
    :return: 所有符合条件的图片坐标，是一个列表（例如：[(960.5, 243.5), (960.5, 243.5),...]）
    """
    try:
        driver.save_screenshot('./image/template.png')
        imsrc = ac.imread('./image/template.png')  # 原始图像
        imsch = ac.imread(imgsch)  # 待查找的部分

        positions = ac.find_all_template(imsrc, imsch)
        cor = []
        if positions is not None:
            for position in positions:
                x, y = position['result']
                cor.append((x, y))
        else:
            raise Exception("Cannot find the images that you provided.")
        return cor
    except Exception as msg:
        print(msg)


def click_according_to_coordinate(driver, x, y, left_click=True):
    """
    根据坐标执行点击操作(web only)
    :param driver:
    :param x: 页面x坐标
    :param y: 页面y坐标
    :param left_click: True为鼠标左键点击，否则为右键点击
    :return:
    """
    try:
        if left_click:
            ActionChains(driver).move_by_offset(x, y).click().perform()
        else:
            ActionChains(driver).move_by_offset(x, y).context_click().perform()
        ActionChains(driver).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前的位置
    except Exception as msg:
        print(msg)


def tap_according_to_coordinate(driver, x, y):
    """
    根据坐标执行点击操作(Mobile device only)
    :param driver:
    :param x: 页面x坐标
    :param y: 页面y坐标
    :return:
    """
    try:
        driver.tap([(x, y)])
    except Exception as msg:
        print(msg)
