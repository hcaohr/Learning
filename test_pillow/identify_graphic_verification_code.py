from PIL import Image
import tesserocr, pytesseract


'''
1. 要调用pytesseract的方法时，必须在script前面加上
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

2. 在windows下安装tesserocr会报错，要通过下载wheel文件来安装
下载链接：https://github.com/simonflueckiger/tesserocr-windows_build/releases
pip3 install tesserocr-2.4.0-cp37-cp37m-win32.whl

3. 安装 tesseract，下载版本要和tesserocr对应起来
下载链接：https://digi.bib.uni-mannheim.de/tesseract/

4. 安装tesserocr遇到的问题：https://www.imooc.com/article/45278
'''

im = Image.open('verification code 1.JPG')

# 把彩色图像转化为灰度图像。RBG转化到HSI彩色空间，采用I分量
gray = im.convert('L')
#gray.show()

# 二值化处理
threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = gray.point(table, '1')
out.save('captcha.jpg')
th = Image.open('captcha.jpg')
# 使用Tesseract进行图片识别
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
print(pytesseract.image_to_string(th))
print(tesserocr.image_to_text(th))
