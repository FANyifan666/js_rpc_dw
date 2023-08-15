import execjs
import requests
import json
import time
# 调用 js实现sign 得到 参数
import requests


def get_data_fan(params):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "AppId": "h5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Origin": "https://m.poizon.com",
        "Pragma": "no-cache",
        "Referer": "https://m.poizon.com/",
        "SK": "9MKtBQ8Eb05dX0dejZM3Wr8AxLc2qMIGJpzSgTzBPlmLwzvjGIjcvPlRAzoWX1oHNt862ESkW7PG8OWRChkjAe6WQh1u",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "appVersion": "5.19.0",
        "ltk": "FMONwpbDpcOjNsKDw6rDs8KrQcKrwo3CvsOsc8OmwpfCkMKgNzXCn3jDk8OlKMOPLw3CuwHCpi7DgsOHwqgcBcKUNR/DnMKCw5LCjsO4w77CoMK+",
        "platform": "h5",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sessionid": "ifsg1scm-rg4o-4tpb-puxs-5ilyegvr80mj1k7q",
        "shumeiId": "BQ+1PPcTD+h8kxQCvrZcbvGRtaHHdCPjjUOXLiIYKokrKLd4Sh6/BgDOt8yr7bNmZ6e+A3IBeTbfMGgpD9KydZA==",
        "sks": "1,hdw3"
    }
    cookies = {
        "sajssdk_2015_cross_new_user": "1",
        "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22189f82d8a9e8b9-0dc243d86373408-26031b51-1296000-189f82d8a9fae3%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5ZjgyZDhhOWU4YjktMGRjMjQzZDg2MzczNDA4LTI2MDMxYjUxLTEyOTYwMDAtMTg5ZjgyZDhhOWZhZTMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22189f82d8a9e8b9-0dc243d86373408-26031b51-1296000-189f82d8a9fae3%22%7D"
    }
    # url = "https://app.poizon.com/api/v1/h5/search/fire/search/list?" + 'data=qIMtbaVEUZOlbiUjypE8K7rvSd8JokVK5pFohyV9ACckjqITcPz0YA​6035410750163AE5C9160E3EEF90D8EC08D9327A4B3BF0E3E40E0488C4896F1F9019AE499B52B341A6D20A8641F6694A816306BD4CE3608C44CA3CEB68B30510A9AB3ED26EFC91BE51680DB57120ED5EFE9EED4F46991B42590D35C23D29F97A58C5F48547862782D7BCF7CA6A27722F1E33153EBE702093AA0542648FE25E973A3133CDE0F394A7AFD0002F444AA25529B5AE53E91DD86AE7D845C69B6C548580008A31CD65E965FD1DC5BD726F9D16FB4A76B2CA49F23EB5CACF40246B5C75453D239D524BFD1CBB17539D69C8CAD104BD6BEA8F4CD44229DE106209613BA681916A5FB59D76D5C49A70879C9C20E366F8CCC0138F8663C4B00840959E69F14C05DD3E3F5750955749191C281D7D4637609A0262C6DA8F458F683627A9702AA4F3E99D5D658A6F3F5E1C614908D3E35F7CE2EB284D200B732298DBFCB580B232D7C1E076F1729DFC296AC334EF16A46C885C143C493E14F4899519282CEE0B243ADB8C117727DD3ED18335CF4C1F02DD887F9CDCC1D8CE51D637D8A7BE0C2F8073201E0F16BC434AE4683666ABEC93FE5BB6E4DBC916DD9FDE7B4BE85BD0048042D98AC03C72109640242480E37F4A7B86A6B37E7A43BF0923469BA59470A2C460E0A854AC190EFF4B4B1B51B0802E0AED8409E17299AFB42E4AD635C1097DDE159E9890BAB5982748CEF3FD7A10445F833DC9362794D0411F6EFE7636CFB62370F1B98EA50F09B17FA7FDEE6F8D43771BD4F13AF05DE35F8A799D9FF13EEDA044982AABDF8216AAC496FF5804F75216D46A45CC9BB1495A5F30DD448DE797DA57A4B7292A5928E81D23B904ACA67CF8DA109D765EC6414D697E1981C529D73E82DFD7082730016AA2ED5F09D9B5C2321B60EC8E52626027F1D0B8F35A1E1948588A12D408AD086B6F431F088C5A0E827B077DEE21FB68D9E81AEE9B345561B3E022AF6E8C683D9243E5796BA238445FE4DD58FD30538FDC1ECACE8F4E1AFFE632F82BA9A7ECDFCF6D35E79BC6766553994EB19B593B8E64FD27862AB8BD3C3B1ACFDECBA760794D12427B428B9AE427DA5A34D4062DED27BF3D52BB85F0F4C33EC846A1CAA14674CC50D5CF71E41378771E68338B4C23B6F8EC8137D551012F1C849CB9A407D14B8C3FE9E2C3DF17A45F3D5DE37A85693112C8056CF1FEBC908AC75EF10F48A4A194290277262197D01FE853F989A5230391577BBF7725DDE83CA683735711984D207010AC5D0C3FDD01F22AD7A3C8323B6DF144B810A137ADC70EEE22DDC683B53E86C5C53BB4E431074BBFC3DBEB155F1B7E3BC4E5382C248BB008B6866D7719E59144C8E9C1BE0B979EAD9923DCAFC331BC2AE3D3FA12DE59167DD746187371560ADE4290B09F4F4191910AB39E08A3E6FE30D5C5139537C300A0E9F585D84204943379B53D8A87984DAFDD89D8ACA284072A9C77EBB18594E2C17D176F284BABDC3A96655BE0649DDC2B09EE85A55ACE3EBFFEF40935'
    url = "https://app.poizon.com/api/v1/h5/search/fire/search/list?"

    params = {
        'data':json.loads(params)['data']
    }

    # print(url)
    response = requests.get(url, headers=headers,params=params, cookies=cookies, proxies=proxies, verify=False)
    print(response.request.url)
    print(response.text)

    return response.text

def get_data(m):
    #请求自己的webserver
    url = 'http://127.0.0.1:8000/get?project_name=dw'
    headers = {'Content-Type': 'application/json'}
    #携带 可变数据
    resp = requests.post(url=url,headers=headers,json=m,verify=False).json()
    print(resp)
    return resp

def get_request(m):
    #   参数
    all_info =get_data(m) #得到请求携带加密参数集合
    # print(all_info)
    #取出 携带：daata
    params =  all_info['d']
    print(params)

    originKey = all_info['a']
    #需要解密的数据
    data_encrypt = get_data_fan(params)
    print(data_encrypt)


    rest = de_data(data_encrypt, originKey)
    print(rest)

def de_data(data,iv):
    js = execjs.compile(open("./解密.js", mode="r", encoding="utf-8").read())
    sign = js.call('de_data', data,iv)
    return sign

def getsign(t):
    #调用js sign文件
    js = execjs.compile(open("./sign算法.js", mode="r", encoding="utf-8").read())
    sign = js.call('get_sign', t)
    # print(sign)
    return sign

if __name__ == '__main__':
    # 代理
    proxies = {
        'http': 'http://127.0.0.1:9888',
        'https': 'http://127.0.0.1:9888'
    }
    #md5的参数
    t = {
    "title": "苹果14pro",
    "page": 0,
    "sortType": 0,
    "sortMode": 1,
    "limit": 20,
    "showHot": 1,
    "enhancedSearch": 0
}
    sign = getsign(t)
    m = {
        "sign": sign,
        "title": "苹果14pro",
        "page": 0,
        "sortType": 0,
        "sortMode": 1,
        "limit": 20,
        "showHot": 1,
        "enhancedSearch": 0
    }
    print(m)
    get_request(m)


"""
(function () {
    // 浏览器逻辑:
    let ws = new WebSocket("ws://127.0.0.1:8848/regist.ws?name=dw");
    // 有人传输数据过来的时候自动执行的函数
    ws.onmessage = function (msg) {
        console.log("发送的消息是" ,JSON.parse(msg.data));
        let data = JSON.parse(msg.data)
        // 当接受到消息后. 进行各种计算.
        // '
        let ret = window.dw.Fun110(JSON.stringify(data), "GET"); // 你得找到加密入口...
        console.log("计算完毕, 结果是", JSON.stringify(ret));
        // 返回结果
        ws.send(JSON.stringify(ret));
    }
})();
"""