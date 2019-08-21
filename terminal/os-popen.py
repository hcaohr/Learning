import os


'''
方法一 - os.popen()

os.popen(cmd, mode, bufsize)
# cmd - 使用的命令。
# mode - 模式权限可以是 'r'(默认) 或 'w'.
# bufsize - 指明文件需要的缓冲大小：
#            0-无缓冲；1-行缓冲；
#            其它正值表示使用参数大小的缓冲（大概值，以字节为单位）
#            负的bufsize意味着使用系统的默认值.
#           一般来说，对于tty设备，它是行缓冲；
#            对于其它文件，它是全缓冲. 如果没有改参数，使用系统的默认值.
# 返回一个文件描述符号为 fd 的打开的文件对象.
'''

result = os.popen('adb devices').readlines()
print(result) # 输入为列表，例如：['List of devices attached\n', 'CB5A29H5XA\tdevice\n', '\n']
