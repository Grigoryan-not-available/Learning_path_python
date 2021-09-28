# import asyncio
# async def print_nums():
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         await asyncio.sleep(0.1)
#
# async def print_time():
#     count_sec = 0
#     while True:
#         if count_sec % 3 == 0:
#             print(f'{count_sec} seconds have passed')
#         count_sec += 1
#         await asyncio.sleep(1)
#
# async def main():
#     tasks = [asyncio.create_task(print_nums()), asyncio.create_task(print_time())]
#     await asyncio.gather(*tasks)
#
# if __name__ == '__main__':
#     # loop = asyncio.get_event_loop()
#     # loop.run_until_complete(main())
#     # loop.close()
#     asyncio.run(main())

#####################################

import requests
from time import time
import asyncio
import aiohttp

url = 'https://loremflickr.com/320/240/dog'

def get_file(url):
    req = requests.get(url, allow_redirects=True)
    return req

def sync_write_image(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)

def main(url, n):
    t0 = time()
    for i in range(n):
        sync_write_image(get_file(url))
    print(f'Sync time = {time() - t0}')

#########################################

def async_write_image(data):
    filename = f'file-{int(time() * 1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)

async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        async_write_image(data)

async def main2(url, n):
    t0 = time()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(n):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)
    print(f'Async time = {time() - t0}')


if __name__ == '__main__':
    main(url, 100)
    #asyncio.run(main2(url, 10))                  #errors on windows
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main2(url, 1000))
