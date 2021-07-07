# from time import sleep


# def hello():
#     print('Hello')
#     sleep(3)
#     print('World!')

# if __name__ == '__main__':
#     hello()

# import asyncio
# loop = asyncio.get_event_loop()


# @asyncio.coroutine
# def hello():
#     print('Hello')
#     yield from asyncio.sleep(3)
#     print('World!')

# if __name__ == '__main__':
#     loop.run_until_complete(hello())

import asyncio
import time
# loop = asyncio.get_event_loop()


# async def hello():
#     print('Hello')
#     await asyncio.sleep(3)
#     print('World!')

# if __name__ == '__main__':
#     # loop.run_until_complete(hello())
#     coroutine = hello()
#     start = time.time()
#     for i in range(5):
#         # asyncio.run(hello())
#         coroutine.send(None)
#     print(f'\n {time.time() - start}')


async def count_to_three():
    print("Веду отсчёт. 1")
    await asyncio.sleep(0)
    print("Веду отсчёт. 2")
    await asyncio.sleep(0)
    print("Веду отсчёт. 3")
    await asyncio.sleep(0)

coroutine_counter = count_to_three()
print(coroutine_counter)  # <coroutine object count_to_three at 0x7f5a58486a98>
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 1"
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 2"
coroutine_counter.send(None)  # Выведет "Веду отсчёт. 3"