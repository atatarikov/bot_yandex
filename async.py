
import asyncio
import time


def fun1(x):
    # print(x**2)
    time.sleep(3)
    print('fun1 завершена')


def fun2(x):
    # print(x**0.5)
    time.sleep(3)
    print('fun2 завершена')


def main():
    fun1(4)
    fun2(4)


print(time.strftime('%X'))

main()

print(time.strftime('%X'))

print('Начало async')


async def fun1_(x):
    # print(x**2)
    await asyncio.sleep(3)
    print('fun1_ завершена')


async def fun2_(x):
    # print(x**0.5)
    await asyncio.sleep(3)
    print('fun2_ завершена')


async def main_():
    task1 = asyncio.create_task(fun1_(4))
    task2 = asyncio.create_task(fun2_(4))

    await task1
    await task2


print(time.strftime('%X'))

asyncio.run(main_())

print(time.strftime('%X'))
