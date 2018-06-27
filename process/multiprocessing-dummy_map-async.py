from multiprocessing.dummy import Pool as ThreadPool
import time

def func(msg):
    print('msg: ', msg)
    time.sleep(1)
    print('********')
    return 'func_return: %s' % msg


if __name__ == '__main__':
    #map_async
    print('\n--------map_async----------')
    args = [1, 2, 10, 11, 18]
    async_pool = ThreadPool(processes=4)
    result = async_pool.map_async(func, args)
    print(result.ready())  # 线程函数是否已经启动了
    print('map_async: 不堵塞')
    result.wait()   # 等待所有线程函数执行完毕
    print('after wait')
    if result.ready():  # 线程函数是否已经启动了
        if result.successful():  # 线程函数是否执行成功
            print(result.get())  # 线程函数返回值