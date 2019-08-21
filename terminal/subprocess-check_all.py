import subprocess

'''
subprocess.check_call() - 用法与subprocess.call()类似，区别是，当返回值不为0时，直接抛出异常.
'''

status2 = subprocess.check_call('adb devices', shell=True)
print(status2) # 0

status1 = subprocess.check_call('dfdadas', shell=True) # 出错，异常.