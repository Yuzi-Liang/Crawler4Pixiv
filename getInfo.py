import urllib.request, urllib.error
import time
import re
import config

findFollow = re.compile(r'"total":(\d+?),')
findBookmark = re.compile(r'"bookmarkCount":(\d+?),')
findLike = re.compile(r'"likeCount":(\d+?),')
findView = re.compile(r'"viewCount":(\d+?),')


head = {
    'cookie': config.cookie,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}

baseurl = 'https://www.pixiv.net/artworks/'


def GetLike(id):
    url = baseurl + str(id)
    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
        html = str(html)
        # print(response)
        # print(html)
        # follow = re.findall(findFollow, html)[0]
        # print(follow)
        likeCount = re.findall(findLike,html)[0]
        return int(likeCount)

    except urllib.error.HTTPError as e:
        if hasattr(e, 'headers'):
            print(e.headers)
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        time.sleep(120)
        response = urllib.request.urlopen(request)
        html = response.read()
        html = str(html)
        likeCount = re.findall(findLike, html)[0]
        return int(likeCount)

    # except urllib.error.URLError as e:
    #     if hasattr(e, "code"):
    #         print(e.code)
    #     if hasattr(e, "reason"):
    #         print(e.reason)
    #     return 0

def GetBookmark(id):
    url = baseurl + str(id)
    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
        html = str(html)
        # print(response)
        # print(html)
        # follow = re.findall(findFollow, html)[0]
        # print(follow)
        bookmarkCount = re.findall(findBookmark,html)[0]
        return int(bookmarkCount)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        return 0

def GetView(id):
    url = baseurl + str(id)
    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
        html = str(html)
        # print(response)
        # print(html)
        # follow = re.findall(findFollow, html)[0]
        # print(follow)
        viewCount = re.findall(findView,html)[0]
        return int(viewCount)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        return 0

# print(GetView('88823520'))


urlShow = 'https://www.pixiv.net/ajax/user/' + config.userID + '/following?offset=0&limit=24&rest=show&tag=&lang=zh'
urlHide = 'https://www.pixiv.net/ajax/user/' + config.userID + '/following?offset=0&limit=24&rest=hide&tag=&lang=zh'


def getHideFollow():
    request = urllib.request.Request(urlHide, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
        html = str(html)
        # print(response)
        # print(html)
        follow = re.findall(findFollow, html)[0]
        # print(follow)
        return int(follow)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)




def getShowFollow():
    request = urllib.request.Request(urlShow, headers=head)
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
        html = str(html)
        # print(response)
        # print(html)
        follow = re.findall(findFollow, html)[0]
        # print(follow)
        return int(follow)

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    pass





# getHideFollow()
# getShowFollow()