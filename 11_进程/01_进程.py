import multiprocessing
import os
import time

# 进程之间不共享全局变量
g_num = []


def my_write():
    """向全局变量g_num写数据"""
    global g_num
    for i in range(5):
        g_num.append(i)


def my_read():
    """读取全局变量g_num的值"""
    global g_num
    print(g_num)


# 如果将上述代码用分进程运行，则第一个会写入数据，但读取的函数读取不到。
# 进程中都是操作自己进程中的全局变量，不会对其他进程中的全局变量产生影响，只不过进程间全局变量的名字相同而已

def dance(count):
    print(os.getpid())  # 获取进程id,在这个函数中相当于主进程
    print(os.getppid())  # 获取父进程id

    for i in range(count):
        time.sleep(1)
        print("dance", i)


def sing(count):
    print(os.getpid())  # 获取进程id,在这个函数中相当于主进程
    print(os.getppid())  # 获取父进程id

    for i in range(count):
        time.sleep(1)
        print("sing", i)

# 主进程默认等待子进程结束后结束
# 让子进程随着主进程的销毁而结束：1、守护主进程：子对象.daemon=True 2、销毁子进程，子进程对象.terminate()
if __name__ == '__main__':
    print(os.getpid())  # 获取主进程ID

    # 子进程中有参数的话，为元组，如果是单个参数，记得加上“，”，kwargs：字典，key值要和函数中的形参完全重名
    my_dance = multiprocessing.Process(target=dance, kwargs={"count": 5})
    my_sing = multiprocessing.Process(target=sing, name="老王", args=(5,))
    # 知道子进程是由哪个主进程创建的（子进程需要主进程回收资源）
    # os.getpid()获取当前进程id
    # os.getppid()获取当前父进程id

    #设置守护进程,一定要在start之前
    my_sing.daemon=True
    my_dance.daemon=True

    #手动设置
    my_dance.terminate()
    my_sing.terminate()

    my_dance.start()
    my_sing.start()


