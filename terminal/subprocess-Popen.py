import subprocess


'''
参考链接： https://www.aiuai.cn/aifarm949.html

方法二 - subprocess 模块

class subprocess.Popen(args,
                       bufsize=-1,
                       executable=None,
                       stdin=None,
                       stdout=None,
                       stderr=None,
                       preexec_fn=None,
                       close_fds=True,
                       shell=False,
                       cwd=None,
                       env=None,
                       universal_newlines=False,
                       startupinfo=None,
                       creationflags=0,
                       restore_signals=True,
                       start_new_session=False,
                       pass_fds=(),
                       *,
                       encoding=None,
                       errors=None)

args：要执行的命令或可执行文件的路径. 一个由字符串组成的序列（通常是列表），列表的第一个元素是可执行程序的路径，剩下的是传给这个程序的
参数，如果没有要传给这个程序的参数，args 参数可以仅仅是一个字符串。
bufsize: 0无缓冲, 1行缓冲，其它正值 缓冲区大小，负值 采用默认系统缓冲（一般是全缓冲）；
executable：如果这个参数不是 None，将替代参数 args 作为可执行程序；
stdin：指定子进程的标准输入；
stdout：指定子进程的标准输出；
stderr：指定子进程的标准错误输出；
preexec_fn：默认是None，否则必须是一个函数或者可调用对象，在子进程中首先执行这个函数，然后再去执行为子进程指定的程序或Shell.
close_fds：布尔型变量，为 True 时，在子进程执行前强制关闭所有除 stdin，stdout和stderr外的文件；
shell：布尔型变量，明确要求使用shell运行程序，与参数 executable 一同指定子进程运行在什么 Shell 中 —— 如果executable=None 而
shell=True，则使用 /bin/sh 来执行 args 指定的程序；也就是说，Python首先起一个shell，再用这个shell来解释指定运行的命令.
cwd：代表路径的字符串，指定子进程运行的工作目录，要求这个目录必须存在；
env：字典，键和值都是为子进程定义环境变量的字符串；
universal_newline：布尔型变量，为 True 时，stdout 和 stderr 以通用换行（universal newline）模式打开；
startupinfo：见下一个参数；
creationfalgs：最后这两个参数是Windows中才有的参数，传递给Win32的CreateProcess API调用.
'''

proc = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

buff = proc.stdout.readlines()
print(buff) # 输入为列表，例如：[b'List of devices attached\r\n', b'CB5A29H5XA\tdevice\r\n', b'\r\n']

print(buff[1].decode().split('\tdevice')) # 读取的列表为bytes格式，需要解码为字符串格式