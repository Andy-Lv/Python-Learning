# 互斥锁是让线程去竞争一个锁，抢到锁的线程先执行，后续继续抢
# 保证同一时刻只有一个线程在运行

import threading

g_num = 0

# 创建锁
mutex = threading.Lock()


def sum_num1():
    global g_num
    # 上锁
    mutex.acquire()

    for i in range(100000):
        g_num += 1

    # 解锁
    mutex.release()  # 如果不解锁就会产生死锁问题，会让此线程一直占用CPU，其他线程无法调用cpu

    print("sum_num1:", g_num)


def sum_num2():
    global g_num

    # 上锁,同一把锁必须解锁才能再上锁
    mutex.acquire()

    for i in range(100000):
        g_num += 1

    # 解锁
    mutex.release()  #

    print("sum_num2:", g_num)


if __name__ == '__main__':
    sub_num1 = threading.Thread(target=sum_num1)
    sub_num2 = threading.Thread(target=sum_num2)

    sub_num1.start()
    sub_num2.start()
