from functools import partial
import asyncio
import os
from concurrent.futures import ThreadPoolExecutor


async def rm(path, executor: ThreadPoolExecutor):
    loop = asyncio.get_event_loop()
    loop.run_in_executor(
        executor, partial(os.remove, path)
    )
