import time
import threading  # 线程模块


# 线程之间的执行是无序的
# 主线程会等待所有的子线程执行完后在结束
# 线程之间共享全局变量

def dance(count):
    for i in range(count):
        time.sleep(1)
        print("dance", i)


def sing(count):
    for i in range(count):
        time.sleep(1)
        print("sing", i)


if __name__ == '__main__':
    my_dance = threading.Thread(target=dance, args=(5,), daemon=True)
    my_sing = threading.Thread(target=sing, kwargs={"count": 5}, daemon=True)

    # 守护主线程 1、daemon=True 2、setDaemon
    my_sing.setDaemon()
    my_dance.setDaemon()

    my_sing.start()
    # 当两个线程对同一个全局变量操作时，会出现竞争cpu进行计算的行为，导致最后计算的数据结果不正确
    # 为了解决这个问题
    # 让主线程先执行第一个线程之后再执行下一个线程
    my_sing.join()

    my_dance.start()
