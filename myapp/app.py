from aiohttp import web

async def get_nav_value(request):
    # 在这里处理获取导航值的逻辑
    return web.json_response({"message": "This is the navigation value"})

app = web.Application()
app.router.add_get('/nav_value', get_nav_value)

if __name__ == "__main__":
    web.run_app(app)
