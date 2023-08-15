from sanic import Sanic, HTTPResponse
import websockets
import asyncio
app = Sanic(__name__)
import json


@app.route("/get", methods=["GET", "POST"])
async def func(req):
    # 在这里. 你可以接受参数. 指定哪个项目 rs4
    # 在url上面传参过来
    project_name = req.args.get("project_name")
    # 我制定的规则是:
    #   url上面传递的参数: project_name.
    #   该项目需要的其他参数, 全部通过json的形式传递过来
    # 强制规定了. 有参数必须走post. 参数通过json传递过来....
    # 此时浏览器上就无法完成测试了....
    project_params = req.json  # {url: "xxxxx"}
    if not project_params:
        project_params = "没参数"

    if project_name:
        async with websockets.connect(f"ws://127.0.0.1:8848/invoke.ws?name={project_name}") as ws:
            await ws.send(json.dumps(project_params))  # 发送数据过去
            print("连接成功了")
            ret = await ws.recv()
        return HTTPResponse(ret)
    else:
        return HTTPResponse("至少要给我一个project_name")


if __name__ == '__main__':
    app.run()
