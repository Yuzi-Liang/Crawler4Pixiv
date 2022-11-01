import urllib.request, urllib.error
import math
import re
import getInfo
import config

findUID = re.compile(r'\{"userId":"(\d+?)",')


def findFollow(mode):
    urls = 'https://www.pixiv.net/ajax/user/' + config.userID + '/following?offset='
    urlm1 = '&limit=100'
    urlm2 = '&rest='
    urle = '&tag=&lang=zh'
    follows = []
    if mode == 1:
        smode = 'hide'
        follow = getInfo.getHideFollow()
    else:
        smode = 'show'
        follow = getInfo.getShowFollow()
    for i in range(0,math.ceil(follow/100)):
        num = i*100
        url = urls + str(num) + urlm1 + urlm2 + smode + urle
        res = askUrl(url)
        html = str(res.read())
        # print(res.read())
        # print(html)
        fos = re.findall(findUID,html)
        # print(fos)
        # print(len(fos))
        follows.extend(fos)
        # print(follows)
        # print(len(follows))
    return follows


def askUrl(url):
    head = {
        'cookie': config.cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    }
    request = urllib.request.Request(url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        # html = response.read()
        # print(response)
        # print(html)
        return response

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    pass

# findFollow(2)