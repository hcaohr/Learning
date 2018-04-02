import subprocess

child = subprocess.Popen(['ping', '-c', '4', 'blog.linuxeye.com'])
child.wait()
print('parent process')