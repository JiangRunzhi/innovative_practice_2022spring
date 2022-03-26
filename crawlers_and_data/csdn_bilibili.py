import requests

header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0",
		  "Cookie": ""}
comments = []
original_url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&oid=894712303&sort=2&pn="

for page in range(1, 10):   # 页码这里就简单处理了
    url = original_url + str(page)
    print(url)
    try:
        html = requests.get(url, headers=header)
        data = html.json()
        if data['data']['replies']:
            for i in data['data']['replies']:
                comments.append(i['content']['message'])
    except Exception as err:
        print(url)
        print(err)

for comment in comments:
    print(comment)
# ————————————————
# 版权声明：本文为CSDN博主「DilicelSten」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Totoro1745/article/details/109908334