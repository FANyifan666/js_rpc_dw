
(function(){
    // 浏览器逻辑:
    let ws = new WebSocket("ws://127.0.0.1:8848/regist.ws?name=xhs");

    // 有人传输数据过来的时候自动执行的函数
    ws.onmessage = function(msg){
        // console.log("我很高兴, 有人给我发消息", msg.data);
        // 当接受到消息后. 进行各种计算.
        let s = '/api/sns/web/v1/search/notes';
        let i =''
        let ret = window._webmsxyw(s,i); // 你得找到加密入口...
        console.log("计算完毕, 结果是",  ret);
        // 返回结果
        ws.send(ret);
    }
})();

(function(){
    // 浏览器逻辑:
    let ws = new WebSocket("ws://127.0.0.1:8848/regist.ws?name=iwencai_xia");

    // 有人传输数据过来的时候自动执行的函数
    ws.onmessage = function(msg){
        // console.log("我很高兴, 有人给我发消息", msg.data);
        // 当接受到消息后. 进行各种计算.
        let ret = window.qiaofu(); // 你得找到加密入口...
        console.log("计算完毕, 结果是",  ret);
        // 返回结果
        ws.send(ret);
    }
})();

//pdd拼多多
let ws = new WebSocket("ws://127.0.0.1:8848/regist.ws?name=pdd");

    // 有人传输数据过来的时候自动执行的函数
    ws.onmessage = function(msg){
        // console.log("我很高兴, 有人给我发消息", msg.data);
        // 当接受到消息后. 进行各种计算.

        let rets;

        fan.messagePackSync(parseInt(Date.now() * 1000)).then(function ret(params) {
            rets =  params
        })
         setTimeout(function() {
          console.log("计算完毕, 结果是",  rets);        ws.send(rets);
}, 100);
        // 返回结果

    }