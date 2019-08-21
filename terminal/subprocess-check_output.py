import subprocess

'''
subprocess.check_output() - 用法与subprocess.call()、subprocess.check_call()类似，区别是，××如果当返回值为0时，直接返回输出结果，如果返回值不为0，直接抛出异常**.

subprocess.check_output() 仅在python3.x中才有.
'''

status2 = subprocess.check_output('adb devices', shell=True)
print(status2) # 0

status1 = subprocess.check_output('dfdadas', shell=True) # 出错，异常.