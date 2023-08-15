// var b = window.dw || {}, v = b.Fun110(JSON.stringify(m), i)

// 通过api/v1/h5/search/fire/search/list 单步调试
// js rpc 解密


// window.dw.Fun110(JSON.stringify(m), i)


(function () {
    // 浏览器逻辑:
    let ws = new WebSocket("ws://127.0.0.1:8848/regist.ws?name=dw");

    // 有人传输数据过来的时候自动执行的函数
    ws.onmessage = function (msg) {
        console.log("发送的消息是" ,msg.data);
        // 当接受到消息后. 进行各种计算.
        // '
        let ret = window.dw.Fun110(JSON.stringify(msg.data), "GET"); // 你得找到加密入口...
        console.log("计算完毕, 结果是", ret);
        // 返回结果
        ws.send(ret);
    }
})();