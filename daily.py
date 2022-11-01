import findPID
import time
import os
import urllib.request,urllib.error
import re


basePath = r'/usr/share/nginx/od/ML/'
baseurl = 'https://www.pixiv.net/artworks/'

findUrl = re.compile(r'"original":"(.+?)"},"tags"',re.S)
findAfter = re.compile(r'"original":"(.*)',re.S)
#findImgurl = re.compile(r'[a-zA-z]+://[^\s]*')
findName = re.compile(r'"illustTitle":"(.+?)"')
findP = re.compile(r'"pageCount":([0-9]+?),"bookmarkCount"',re.S)
findType = re.compile(r'_p\d*.(\w*)')
#findR18 = re.compile(r'"toggle_novel_r18_genre_page":(.+?),')
#findGifUrl = re.compile(r'"regular":"(.+?)"',re.S)
findID = re.compile(r'/(\d+?)_')
findPage = re.compile(r'"/(\d+?)"')
findGifType = re.compile(r'ugoira0.(.+)')

def advAskRes(url):
    head = {
        'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh-HK;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'referer': 'https://www.pixiv.net/artworks/84073765',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }

    request = urllib.request.Request(url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        # print(response)
        # print(html)
        return response
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


def askURL(url):
    head = {
        "refer": "https://www.pixiv.net/ranking.php?mode=daily&content=illust",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
    }

    request = urllib.request.Request(url,headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        #print(response)
        #print(html)

        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html






def getData(baseurl):  #获取数据并保存
    html = askURL(baseurl)
    # print(html)
    # soup = BeautifulSoup(html,'html.parser')
    html = str(html)
    # print(html)
    # print(re.findall(findP,html))
    # print(len(re.findall(findP,html)))
    # testlist = re.findall(findPage,html)
    # print(testlist)
    # print(html)
    pageList = re.findall(findP, html)
    # print(pageList)
    print('This illustration has %dp' % int(pageList[0]))

    url = str(re.findall(findUrl, html)[0])
    # title = str(re.findall(findName,html)[0])
    title = str(i) + '_' + str(re.findall(findID, url)[0])
    print('pid = %s' % title)

    # R18 = re.findall(findR18, html)[0]
    # print("是否为R18:%s" %R18)

    # for page in range(0, 2):
    r = 0
    for page in range(0, int(pageList[0])):
        thisurl = url.replace('p0', 'p%d' % page)
        print('Visiting %s' % thisurl)

        try:
            try:
                type = re.findall(findType, thisurl)
                if os.path.exists('%s_p%d.%s' % (title, page, type[0])):
                    print('File already exists!')
                    r = 1
                    continue
                else:
                    img = advAskRes(thisurl)
                    print('Image format is %s' % type[0])
                    f = open('%s_p%d.%s' % (title, page, type[0]), 'wb')
                    f.write(img.read())
                    f.close()
                    print('\033[92m Save successfully\n \033[0m')
                    r = 0
            except:
                if url.find('ugoira0') != -1:
                    # print('此图片获取出现问题')
                    print('This image is gif，trying to save the static image\n')
                    # print(html)
                    # print(url)
                    # type = re.findall(findGifType,url)
                    type = ['jpg']
                    gifurl0 = url.replace('original', 'master')
                    # print(gifurl0)
                    gifurl1 = gifurl0.replace('png', 'jpg')
                    gifurl = gifurl1.replace('ugoira0', 'master1200')
                    # print(gifurl)
                    # type = ['jpg']
                    print('Image format is %s' % type[0])
                    if os.path.exists('%s_p%d.%s' % (title, page, type[0])):
                        print('File already exists!')
                        r = 1
                        continue
                    else:
                        img = advAskRes(gifurl)
                        f = open('%s_p%d.%s' % (title, page, type[0]), 'wb')
                        f.write(img.read())
                        f.close()
                        print('\033[92m Save successfully\n \033[0m')
                        r = 0
                else:
                    print('\033[91m Something is wrong when saving this image \033[0m')
        except:
            print('\033[91m Something is wrong when visiting this url\n \033[0m')
            return 0

    print("Finish downloading\n")
    return r






ids = findPID.findPIDs_by_Daily()
filename = time.strftime("%Y-%m-%d", time.localtime())
savePath = basePath + filename

isExists = os.path.exists(savePath)
print(savePath)
print('isExist = %s',isExists)
if not isExists:
    print('First time，new folder')
    os.makedirs(savePath)
    print('Create folder successfully')
os.chdir('%s' %savePath)

i = 0

maxp = 20
if maxp >= len(ids):
    maxp = len(ids)
    print('Download All!')
elif maxp <= 0:
    print('\033[91m Invalid input!!!!! \033[0m')

for id in ids:
    url = baseurl + id
    if i >= maxp:
        break
    i = i + 1
    try:
        getData(url)
    except:
        print('\033[91m Wrong ID!!!!! \033[0m')


ids = findPID.findPIDs_by_Daily_R18()
filename = time.strftime("%Y-%m-%d", time.localtime())
savePath = basePath + filename + '_R18'

isExists = os.path.exists(savePath)
print(savePath)
print('isExist = %s',isExists)
if not isExists:
    print('First time，new folder')
    os.makedirs(savePath)
    print('Create folder successfully')
os.chdir('%s' %savePath)

i = 0

maxp = 20
if maxp >= len(ids):
    maxp = len(ids)
    print('Download All!')
elif maxp <= 0:
    print('\033[91m Invalid input!!!!! \033[0m')

for id in ids:
    url = baseurl + id
    if i >= maxp:
        break
    i = i + 1
    try:
        getData(url)
    except:
        print('\033[91m Wrong ID!!!!! \033[0m')

ids = findPID.findPIDs_by_Male()
filename = time.strftime("%Y-%m-%d", time.localtime())
savePath = basePath + filename + '_male'

isExists = os.path.exists(savePath)
print(savePath)
print('isExist = %s',isExists)
if not isExists:
    print('First time，new folder')
    os.makedirs(savePath)
    print('Create folder successfully')
os.chdir('%s' %savePath)

i = 0

maxp = 20
if maxp >= len(ids):
    maxp = len(ids)
    print('Download All!')
elif maxp <= 0:
    print('\033[91m Invalid input!!!!! \033[0m')

for id in ids:
    url = baseurl + id
    if i >= maxp:
        break
    i = i + 1
    try:
        getData(url)
    except:
        print('\033[91m Wrong ID!!!!! \033[0m')


ids = findPID.findPIDs_by_Male_R18()
filename = time.strftime("%Y-%m-%d", time.localtime())
savePath = basePath + filename + '_male_R18'

isExists = os.path.exists(savePath)
print(savePath)
print('isExist = %s',isExists)
if not isExists:
    print('First time，new folder')
    os.makedirs(savePath)
    print('Create folder successfully')
os.chdir('%s' %savePath)

i = 0

maxp = 20
if maxp >= len(ids):
    maxp = len(ids)
    print('Download All!')
elif maxp <= 0:
    print('\033[91m Invalid input!!!!! \033[0m')

for id in ids:
    url = baseurl + id
    if i >= maxp:
        break
    i = i + 1
    try:
        getData(url)
    except:
        print('\033[91m Wrong ID!!!!! \033[0m')

ids = findPID.findPIDs_by_Weekly()
filename = time.strftime("%Y-%m-%d", time.localtime())
savePath = basePath + filename + '_w'

isExists = os.path.exists(savePath)
print(savePath)
print('isExist = %s',isExists)
if not isExists:
    print('First time，new folder')
    os.makedirs(savePath)
    print('Create folder successfully')
os.chdir('%s' %savePath)

i = 0

maxp = 50
if maxp >= len(ids):
    maxp = len(ids)
    print('Download All!')
elif maxp <= 0:
    print('\033[91m Invalid input!!!!! \033[0m')

for id in ids:
    url = baseurl + id
    if i >= maxp:
        break
    i = i + 1
    try:
        getData(url)
    except:
        print('\033[91m Wrong ID!!!!! \033[0m')


ids = findPID.findPIDs_by_Weekly_R18()
filename = time.strftime("%Y-%m-%d", time.localtime())
savePath = basePath + filename + '_w_R18'

isExists = os.path.exists(savePath)
print(savePath)
print('isExist = %s',isExists)
if not isExists:
    print('First time，new folder')
    os.makedirs(savePath)
    print('Create folder successfully')
os.chdir('%s' %savePath)

i = 0

maxp = 50
if maxp >= len(ids):
    maxp = len(ids)
    print('Download All!')
elif maxp <= 0:
    print('\033[91m Invalid input!!!!! \033[0m')

for id in ids:
    url = baseurl + id
    if i >= maxp:
        break
    i = i + 1
    try:
        getData(url)
    except:
        print('\033[91m Wrong ID!!!!! \033[0m')



