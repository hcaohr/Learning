"""
进程池的使用有四种方式：apply_async、apply、map_async、map。
其中apply_async和map_async是异步的，也就是启动进程函数之后会
继续执行后续的代码不用等待进程函数返回。apply_async和map_async
方式提供了一写获取进程函数状态的函数：ready()、successful()、get()。
PS：join()语句要放在close()语句后面。
"""
import multiprocessing
import time

def func(msg):
    print('msg: ', msg)
    time.sleep(1)
    print('********')
    return 'func_return: %s' % msg

if __name__ == '__main__':
    #map_async
    print('\n--------map_async----------')
    args = [1, 2, 4, 5, 7, 8]
    pool = multiprocessing.Pool(processes=5)
    return_data = pool.map(func, args)
    print('堵塞')  # 执行完func才执行该句
    pool.close()
    pool.join()
    print(return_data)  # join语句要放在close之后