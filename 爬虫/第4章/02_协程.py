import asyncio
import time


async def func1():
    print("我是函数1号")
    # time.sleep(2)#当程序出现同步操作时,异步中断
    await asyncio.sleep(2)
    print("我是函数1号")


async def func2():
    print("我是函数2号")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("我是函数2号")


async def func3():
    print("我是函数3号")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("我是函数3号")


# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [f1, f2, f3]
#     # 一次性启动多个任务
#     t1=time.time()
#     asyncio.run(asyncio.wait(tasks))
#     t2=time.time()

async def main():
    # 第一种写法
    f1 = func1()
    await f1  # 一般await挂起操作放在协程对象前面

#     第二种写法
    tasks=[func1(),func2(),func3()]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
