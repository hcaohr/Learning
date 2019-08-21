import subprocess


'''
subprocess.call() - 执行命令，并返回执行状态. 其中shell参数为False时，命令需要通过列表的方式传入；当shell为True时，可直接传入命令.
'''

status1 = subprocess.call(['adb','devices'],shell=False)
status2 = subprocess.call('adb devices',    shell=True)
print(status1) # 0
print(status2) # 0