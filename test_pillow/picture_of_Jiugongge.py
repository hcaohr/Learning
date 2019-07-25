from PIL import Image


def fill_image(img_path, new_img_path):
    """ 填充正方形白色背景图片 """
    image = Image.open(img_path)
    width, height = image.size # 获取图片的宽高
    side = max(width, height) # 对比宽和高哪个大

    # 新生成的图片是正方形的,边长取大的,背景设置白色
    new_image = Image.new(image.mode, (side, side), color='white')

    # 根据尺寸不同，将原图片放入新建的空白图片中部
    if width > height:
        new_image.paste(image, (0, int((side - height)/2)))
    else:
        new_image.paste(image, int((side - width)/2), 0)
    new_image.save(new_img_path)


def cut_images(img_path, new_img_path, i=1):
    """ 切割大正方形图 """
    image = Image.open(img_path)
    width, height = image.size
    one_third_width = int(width/3) # 三分之一正方形线像素

    # 保存每一个小切图的区域
    box_list = []

    """ 
    切图区域是矩形，位置由对角线的两个点(左上,右下)确定,
    而 crop() 实际要传入四个参数(left, upper, right, lower) 
    """
    for x in range(3):
        for y in range(3):
            left = x * one_third_width # 左像素
            upper = y * one_third_width # 上像素
            right = (x + 1) * one_third_width # 右像素
            lower = (y + 1) * one_third_width # 下像素
            box = [left, upper, right, lower]
            cut = image.crop(box)
            cut.save(new_img_path.format(i))
            i += 1


#fill_image('../opencv/th2.jpg', 'new_fill_image.jpg')
#cut_images('new_fill_image.jpg', 'crop_{0}.jpg')


