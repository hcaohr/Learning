"""
filter()函数用于过滤序列, 过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
filter()函数接收一个函数 func 和一个iterable(可以是list，字符串等)，这个函数
 func 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动
 过滤掉不符合条件的元素，最后将返回 True 的元素放到新列表中。

关于filter()方法, python3和python2有一点不同
python2中返回的是过滤后的列表, 而python3中返回到是一个filter类
"""

list = [1,2,4,6,8,9]
def is_gt_5(num):
    return num > 5

new_list = filter(is_gt_5, list)
print(new_list) #python2返回[6, 8, 9], python3返回<filter object at 0x000000C15A3FB358>

name = 'pythontab.com 2018'
print(filter(str.isdigit, name)) #python2返回'2018', python3返回<filter object at 0x000000C15A3FB0F0>