import aiofiles
import asyncio
import json
from pathlib import Path

directory = 'files'

async def read_file1(filename):
    cnt = 0
    while cnt < 10:
        async with aiofiles.open(filename, mode='r') as f:
            contents = await f.read()
        print(contents)
        await asyncio.sleep(0.2)
        cnt = cnt + 1
        
async def read_file2(filename):
    while True:
        async with aiofiles.open(filename, mode='r') as f:
            contents = await f.read()
        print(contents)
        await asyncio.sleep(1)
        
    
async def main():
    contents = ''
    tasks = []
    # tasks.append(asyncio.create_task(read_file1(f"{directory}/text1.txt")))
    # tasks.append(asyncio.create_task(read_file2(f"{directory}/text2.txt")))
    tasks.append(asyncio.ensure_future(read_file1(f"{directory}/text1.txt")))
    tasks.append(asyncio.ensure_future(read_file2(f"{directory}/text2.txt")))
    
    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # await asyncio.gather(*tasks)
    
    

asyncio.run(main())