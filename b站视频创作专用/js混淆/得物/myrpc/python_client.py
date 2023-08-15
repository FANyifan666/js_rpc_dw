
# 3. web端
# pip install websockets
import websockets
import asyncio


async def main():
    # python这边链接是为了什么? 为了让ws调用js. 完成加密
    # Python连接websocket服务器的逻辑
    async with websockets.connect("ws://127.0.0.1:8848/invoke.ws?name=xhs") as ws:
        await ws.send("你好, 我叫周杰伦")  # 发送数据过去
        print("连接成功了")
        ret = await ws.recv()
        print(ret)


if __name__ == '__main__':
    asyncio.run(main())
