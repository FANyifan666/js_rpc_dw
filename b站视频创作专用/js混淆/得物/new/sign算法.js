var crypto = require('crypto')

function MD5(e) {
    return crypto.createHash("md5").update(e.toString()).digest("hex")
}

function g(t, e, n) {
    void 0 === e && (e = "048a9c4943398714b356a696503d2d36"),
    void 0 === n && (n = !1);
    var r = function (t, e) {
        return null === e ? void 0 : e
    }
        , i = function (t) {
        if ([void 0, null, ""].includes(t))
            return "";
        if ("[object Object]" === Object.prototype.toString.call(t))
            return JSON.stringify(t, r);
        if (Array.isArray(t)) {
            var e = "";
            return t.forEach((function (n, i) {
                    "[object Object]" === Object.prototype.toString.call(n) ? e += JSON.stringify(n, r) : [void 0, null].includes(n) ? e += null : e += n.toString(),
                    i < t.length - 1 && (e += ",")
                }
            )),
                e
        }
        return t.toString()
    }
        , o = Object.keys(t).sort().reduce((function (e, n) {
            return void 0 === t[n] ? e : e + n + i(t[n])
        }
    ), "");
    return /[\u00A0\u3000]/g.test(o),
        o += e,
        MD5(o)
}

function get_sign(t){
    var e = '048a9c4943398714b356a696503d2d36';  //固定死的
    var n;
// console.log(g(t,e,n))
    return g(t,e,n)
}


//     var e = '048a9c4943398714b356a696503d2d36';  //固定死的
//     var n;
//     var t = {
//     "title": "AJ11白蓝康扣",
//     "page": 0,
//     "sortType": 0,
//     "sortMode": 1,
//     "limit": 20,
//     "showHot": 1,
//     "enhancedSearch": 0
// }
// console.log(g(t,e,n))