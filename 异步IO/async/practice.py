import asyncio

@asyncio.coroutine
def hello():
    print('hello world!')
    r = yield from asyncio.sleep(1)
    print(r)
    print('hello world!')

loop = asyncio.get_event_loop()

loop.run_until_complete(hello())
loop.close()
