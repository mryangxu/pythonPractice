def application(environ, start_responese):
    print(environ)
    start_responese('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % environ['PATH_INFO'][1:] or 'web'
    return [body.encode('utf-8')]