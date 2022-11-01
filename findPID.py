import re
import urllib.request, urllib.error, urllib.parse
import gzip
import config

findID = re.compile(r'"(\d+?)":null')
findDailyID = re.compile(r'<a href="/artworks/(\d+?)"class="t')
findTagID = re.compile(r'"id":"(\d+?)","title":')


def findPIDs_by_Author(pid):
    baseurls = "https://www.pixiv.net/ajax/user/"
    baseurle = "/profile/all?lang=zh"
    PIDs = []
    url = baseurls + str(pid) + baseurle
    res = askUrl(url)
    html = res.read()
    # print(html)
    # print(res)
    # soup = BeautifulSoup(html, 'html.parser')
    #
    # html = str(html)
    # print(html)

    ret = gzip.decompress(html).decode("utf-8")
    # print(ret)

    # print(re.findall(findID,ret))

    PIDs = re.findall(findID,ret)
    print(PIDs)
    print(len(PIDs))
    return PIDs

def findPIDs_by_Daily():
    url = 'https://www.pixiv.net/ranking.php'
    res = askUrl(url)
    html = res.read()
    ret = gzip.decompress(html).decode("utf-8")
    # print(ret)
    PIDs = re.findall(findDailyID,ret)
    print(PIDs)
    print(len(PIDs))
    return PIDs

def findPIDs_by_Daily_R18():
    url = 'https://www.pixiv.net/ranking.php?mode=daily_r18'
    res = askUrl(url)
    html = res.read()
    ret = gzip.decompress(html).decode("utf-8")
    # print(ret)
    PIDs = re.findall(findDailyID,ret)
    print(PIDs)
    print(len(PIDs))
    return PIDs

def findPIDs_by_Weekly():
    url = 'https://www.pixiv.net/ranking.php?mode=weekly'
    res = askUrl(url)
    html = res.read()
    ret = gzip.decompress(html).decode("utf-8")
    # print(ret)
    PIDs = re.findall(findDailyID,ret)
    print(PIDs)
    print(len(PIDs))
    return PIDs

def findPIDs_by_Weekly_R18():
    url = 'https://www.pixiv.net/ranking.php?mode=weekly_r18'
    res = askUrl(url)
    html = res.read()
    ret = gzip.decompress(html).decode("utf-8")
    # print(ret)
    PIDs = re.findall(findDailyID,ret)
    print(PIDs)
    print(len(PIDs))
    return PIDs

def findPIDs_by_Male():
    url = 'https://www.pixiv.net/ranking.php?mode=male'
    res = askUrl(url)
    html = res.read()
    ret = gzip.decompress(html).decode("utf-8")
    # print(ret)
    PIDs = re.findall(findDailyID,ret)
    print(PIDs)
    print(len(PIDs))
    return PIDs

def findPIDs_by_Male_R18():
    url = 'https://www.pixiv.net/ranking.php?mode=male_r18'
    res = askUrl(url)
    html = res.read()
    ret = gzip.decompress(html).decode("utf-8")
    # print(ret)
    PIDs = re.findall(findDailyID,ret)
    print(PIDs)
    print(len(PIDs))
    return PIDs

def findPIDs_by_Female():
    url = 'https://www.pixiv.net/ranking.php?mode=female'
    res = askUrl(url)
    html = res.read()
    ret = gzip.decompress(html).decode("utf-8")
    # print(ret)
    PIDs = re.findall(findDailyID,ret)
    print(PIDs)
    print(len(PIDs))
    return PIDs

def findPIDs_by_Female_R18():
    url = 'https://www.pixiv.net/ranking.php?mode=female_r18'
    res = askUrl(url)
    html = res.read()
    ret = gzip.decompress(html).decode("utf-8")
    # print(ret)
    PIDs = re.findall(findDailyID,ret)
    print(PIDs)
    print(len(PIDs))
    return PIDs

def findPIDs_by_Monthly():
    url = 'https://www.pixiv.net/ranking.php?mode=monthly'
    res = askUrl(url)
    html = res.read()
    ret = gzip.decompress(html).decode("utf-8")
    # print(ret)
    PIDs = re.findall(findDailyID,ret)
    print(PIDs)
    print(len(PIDs))
    return PIDs

def findPIDs_by_Tag():
    tagn = int(input('Please enter number of tag:'))
    mode = input('Please enter search method:\n1.in strict accordance with tag\n2.Keywords can longer than tag\n')
    if mode == '1':
        urle = '&s_mode=s_tag_full&type=all&lang=zh'
    elif mode == '2':
        urle = '&s_mode=s_tag&type=all&lang=zh'
    else:
        print('Invalid input, default method 2')
        urle = '&s_mode=s_tag&type=all&lang=zh'
    sumtag1 = ''
    sumtag2 = ''
    sumtag3 = ''
    # urle = '&s_mode=s_tag&type=all&lang=zh'
    count = 0
    for n in range(0,tagn):
        tag = input('Please enter tag:')
        if tag.find('(') < 0:
            urltag = urllib.parse.quote(tag)
            # urle = '&s_mode=s_tag_full&type=all&lang=zh'
            if count > 0:
                count = count + 1
                sumtag1 = sumtag1 + r'%20' + urltag
                sumtag2 = sumtag1
                sumtag3 = sumtag3 + '_' + tag
            else:
                count = count + 1
                sumtag1 = urltag
                sumtag2 = sumtag1
                sumtag3 = tag
        else:    #如果是带括号的tag
            print('Tag with brackets')
            # urle = '&s_mode=s_tag&type=all&lang=zh'
            tag1 = re.split('\(' ,tag)
            tag1[0] = urllib.parse.quote(tag1[0])
            tag2 = re.split('\)' ,tag1[1])
            tag2[0] = urllib.parse.quote(tag2[0])
            tag2[1] = urllib.parse.quote(tag2[1])
            if count > 0:
                count = count + 1
                sumtag2 = sumtag2 + r'%20' + urllib.parse.quote(tag)
                sumtag1 = sumtag1 + r'%20' + tag1[0] + '(' + tag2[0] + ')' + tag2[1]
                sumtag3 = sumtag3 + '_' + tag
            else:
                count = count + 1
                # print(urllib.parse.quote(tag))
                # print(tag)
                sumtag2 = urllib.parse.quote(tag)
                sumtag1 = tag1[0] + '(' + tag2[0] + ')' + tag2[1]
                sumtag3 = tag
                # print(sumtag2)
                # print(sumtag1)
    sumtag3 = sumtag3 + '_mode' + mode
    urls = 'https://www.pixiv.net/ajax/search/artworks/'
    urlm1 = '?word='
    urlm2 = '&order=date_d&mode=all&p='
    # urle = '&s_mode=s_tag_full&type=all&lang=zh'
    # tag = input('请输入要查找的tag:')

    p = input('Please enter the page you need to download:')
    url = urls + sumtag1 + urlm1 + sumtag2 + urlm2 + p +urle
    # print(sumtag2)
    # print(url)
    res = askUrl(url)
    html = res.read()
    ret = gzip.decompress(html).decode("utf-8")
    # print(ret)
    PIDs = re.findall(findTagID, ret)
    print(PIDs)
    print(len(PIDs))
    PIDs.append(sumtag3)
    return PIDs

def findPIDs_by_Tag_sort():
    tagn = int(input('Please enter number of tag:'))
    mode = input('Please enter search method:\n1.in strict accordance with tag\n2.Keywords can longer than tag\n')
    if mode == '1':
        urle = '&s_mode=s_tag_full&type=all&lang=zh'
    elif mode == '2':
        urle = '&s_mode=s_tag&type=all&lang=zh'
    else:
        print('Invalid input, default method 2')
        urle = '&s_mode=s_tag&type=all&lang=zh'
    sumtag1 = ''
    sumtag2 = ''
    sumtag3 = ''
    # urle = '&s_mode=s_tag&type=all&lang=zh'
    count = 0
    for n in range(0,tagn):
        tag = input('Please enter tag:')
        if tag.find('(') < 0:
            urltag = urllib.parse.quote(tag)
            # urle = '&s_mode=s_tag_full&type=all&lang=zh'
            if count > 0:
                count = count + 1
                sumtag1 = sumtag1 + r'%20' + urltag
                sumtag2 = sumtag1
                sumtag3 = sumtag3 + '_' + tag
            else:
                count = count + 1
                sumtag1 = urltag
                sumtag2 = sumtag1
                sumtag3 = tag
        else:    #如果是带括号的tag
            print('Tag with brackets')
            # urle = '&s_mode=s_tag&type=all&lang=zh'
            tag1 = re.split('\(' ,tag)
            tag1[0] = urllib.parse.quote(tag1[0])
            tag2 = re.split('\)' ,tag1[1])
            tag2[0] = urllib.parse.quote(tag2[0])
            tag2[1] = urllib.parse.quote(tag2[1])
            if count > 0:
                count = count + 1
                sumtag2 = sumtag2 + r'%20' + urllib.parse.quote(tag)
                sumtag1 = sumtag1 + r'%20' + tag1[0] + '(' + tag2[0] + ')' + tag2[1]
                sumtag3 = sumtag3 + '_' + tag
            else:
                count = count + 1
                # print(urllib.parse.quote(tag))
                # print(tag)
                sumtag2 = urllib.parse.quote(tag)
                sumtag1 = tag1[0] + '(' + tag2[0] + ')' + tag2[1]
                sumtag3 = tag
                # print(sumtag2)
                # print(sumtag1)
    sumtag3 = sumtag3 + '_mode' + mode
    urls = 'https://www.pixiv.net/ajax/search/artworks/'
    urlm1 = '?word='
    urlm2 = '&order=date_d&mode=all&p='
    # urle = '&s_mode=s_tag_full&type=all&lang=zh'
    # tag = input('请输入要查找的tag:')
    p = 1
    PIDs = []
    while 1:
        print('page = %d' %p)
        url = urls + sumtag1 + urlm1 + sumtag2 + urlm2 + str(p) + urle
        res = askUrl(url)
        html = res.read()
        ret = gzip.decompress(html).decode("utf-8")
        AddPIDs = re.findall(findTagID, ret)

        PIDs = PIDs + AddPIDs

        if len(AddPIDs) < 60 or p > 999:
            break

        p = p + 1
    PIDs.append(sumtag3)

    # p = input('Please enter the page you need to download:')
    # url = urls + sumtag1 + urlm1 + sumtag2 + urlm2 + p +urle
    # # print(sumtag2)
    # # print(url)
    # res = askUrl(url)
    # html = res.read()
    # ret = gzip.decompress(html).decode("utf-8")
    # # print(ret)
    # PIDs = re.findall(findTagID, ret)
    # print(PIDs)
    # print(len(PIDs))
    # PIDs.append(sumtag3)
    return PIDs


def askUrl(url):
    head = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": config.cookie,
        "referer": "https://www.pixiv.net/users/4338012/following?p=3&rest=hide",
        "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
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











