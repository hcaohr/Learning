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
    #apply
    print('\n--------apply----------')
    pool = multiprocessing.Pool(processes=4)
    results = []
    for i in range(10):
        msg = 'hello world %d' % i
        result = pool.apply(func, (msg, ))
        results.append(result)
    print('appply_async: 堵塞')  # 执行完func才执行该句
    pool.close()
    pool.join()  # join语句要放在close之后
    print(results)