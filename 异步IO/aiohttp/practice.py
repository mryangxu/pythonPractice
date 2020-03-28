import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def index(request):
    await asyncio.sleep(0.5)
    return web.json_response({
        'name': 'index'
    })

@routes.get('/hello')
async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

def init():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host='127.0.0.1', port=8000)

init()