from TestImport_1 import Dog
from TestImport_2 import say_hello as Ts1_hello

Ts1_hello()
dog = Dog

# 当导入多个模块中的相同函数名的函数时，会执行后导入的函数
# 如果必须用两个模块中的同名函数，可以用as起别名
