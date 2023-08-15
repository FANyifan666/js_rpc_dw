
# 中间商....
# pip install websockets
import websockets
import asyncio
import re

browser_info = {}
client_info = {}


async def regist(ws, path):
    # 注意正则最后了. 如果用.*? 会什么都匹配不到
    obj = re.compile(r"/(?P<action>.*?)\.ws\?name=(?P<name>.*)")
    search_result = obj.search(path)
    action = search_result.group("action")
    name = search_result.group("name")
    if action == "regist":  # 来自浏览器
        browser_info[name] = ws  # 保存该链接
        # {`iwencai`: 和`iwencai`浏览器之间的链接}
        return "browser", name

    elif action == 'invoke':
        client_info[name] = ws
        # {`iwencai`: 和`iwencai`客户端之间的链接}
        return "client", name


# 第一个参数ws表示服务器与客户端的链接
# path表示请求过来的路径
async def handle(ws, path):
    # 建立连接的时候走这里.
    # /regist.ws?name=iwencai => 浏览器那边
    # /invoke.ws?name=iwencai => python客户端那边
    t, name = await regist(ws, path)
    async for msg in ws:  # 接受消息
        if t == 'browser':
            # 接受到的消息来自于浏览器
            await client_info[name].send(msg)
        elif t == 'client':
            await browser_info[name].send(msg)


async def main():
    # 启动websocket服务区
    async with websockets.serve(handle, "127.0.0.1", 8848) as flkjdaslkfjadslkjfkladsjflkasd:
        print("你成功的启动了一个websocket")
        await asyncio.Future()  # 永远停在这里.


if __name__ == '__main__':
    asyncio.run(main())

