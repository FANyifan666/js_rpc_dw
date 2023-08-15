import requests
def get_data_fan():
    proxies = {
            'http': 'http://127.0.0.1:9888',
            'https': 'http://127.0.0.1:9888'
        }

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
    url = "https://app.poizon.com/api/v1/h5/search/fire/search/list"
    params = {
        "data": "cDhwrM7YJSHsIy6go9AhEUsSMaHpavoHFUaeh72RdvzFnHAX8p9qRgFgCyAHD1nCgaYwP6IVBdset/8FrUYxUg​7C271755FD611D1531443678C8AD7FF2F9A0FA920400504E662ED417209210E98D427156281EEAD4B98C0B94D6C43596FF3E68191B97E1D2BA756FD9CB0831E769BC5E00261153B5C3AE1C1824EF82A4E384180FF9075EFC07F351B1A8BE476371DC31AF6CA0AAE6BA274446BDCF8DAF936F81D71B933781B2D7C4E0E239A1A873230F9CA6D02CD923BF5DDAA7C40D463683A8955B7ABAAB9B35AC3D3F63E059"}
    response = requests.get(url, headers=headers, cookies=cookies, params=params,proxies=proxies,verify=False)

    print(response.text)
    print(response)