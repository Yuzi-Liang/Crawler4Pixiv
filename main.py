import re
# from bs4 import BeautifulSoup
import urllib.request,urllib.error
import findPID
import findFolow
import getInfo
import os
import sys
import time
import config

basePath = config.savePath

def main():
    baseurl = 'https://www.pixiv.net/artworks/'
    findMethod = input("Method：\n1.Author id\n2.Illustration id\n3.Daily rank\n4.Daily rank R18\n5.Weekly rank\n6.Weekly rank R18\n7.Monthly rank\n8.Daily male rank\n9.Daily male rank R18\n10.daily female rank\n11.Daily female rank R18\n12.Tag\n13.Followed Author in public\n14.Followed Author in private\n15.Followed Author in public without asking\n16.Followed Author in private without asking\n17.Repair by illustration id\n18.Update illustrations of followed author in public\n19.Update illustrations of followed author in private\n20.Tag & sort\n")
    if findMethod == '1':
        pid = input('Please enter author id:')
        ids = findPID.findPIDs_by_Author(pid)
        savePath = basePath + pid
    elif findMethod == '2':
        illid = input('Please enter illustration id:')
        ids = [illid]
        savePath = basePath
    elif findMethod == '3':
        ids = findPID.findPIDs_by_Daily()
        filename = time.strftime("%Y-%m-%d", time.localtime())
        savePath = basePath + filename
    elif findMethod == '4':
        ids = findPID.findPIDs_by_Daily_R18()
        filename = time.strftime("%Y-%m-%d", time.localtime())
        savePath = basePath + filename + '_R18'
    elif findMethod == '5':
        ids = findPID.findPIDs_by_Weekly()
        filename = time.strftime("%Y-%m-%d", time.localtime())
        savePath = basePath + filename + '_w'
    elif findMethod == '6':
        ids = findPID.findPIDs_by_Weekly_R18()
        filename = time.strftime("%Y-%m-%d", time.localtime())
        savePath = basePath + filename + '_w_R18'
    elif findMethod == '7':
        ids = findPID.findPIDs_by_Monthly()
        filename = time.strftime("%Y-%m", time.localtime())
        savePath = basePath + filename
    elif findMethod == '8':
        ids = findPID.findPIDs_by_Male()
        filename = time.strftime("%Y-%m-%d", time.localtime())
        savePath = basePath + filename + '_male'
    elif findMethod == '9':
        ids = findPID.findPIDs_by_Male_R18()
        filename = time.strftime("%Y-%m-%d", time.localtime())
        savePath = basePath + filename + '_male_R18'
    elif findMethod == '10':
        ids = findPID.findPIDs_by_Female()
        filename = time.strftime("%Y-%m-%d", time.localtime())
        savePath = basePath + filename + '_female'
    elif findMethod == '11':
        ids = findPID.findPIDs_by_Female_R18()
        filename = time.strftime("%Y-%m-%d", time.localtime())
        savePath = basePath + filename + '_female_R18'
    elif findMethod == '12':
        ids = findPID.findPIDs_by_Tag()
        filename = ids[-1]
        ids.pop()
        savePath = basePath + filename + '_Tag'
    elif findMethod == '13':
        uids = findFolow.findFollow(2)
        for uid in uids:
            ids = findPID.findPIDs_by_Author(uid)
            savePath = basePath + uid

            isExists = os.path.exists(savePath)
            if not isExists:
                os.makedirs(savePath)
            os.chdir('%s' % savePath)

            i = 0

            maxp = int(input("Please enter the number of illustrations you need to download:"))
            if maxp >= len(ids):
                maxp = len(ids)
                print('Download All!')
            elif maxp <= 0:
                print('\033[91m Invalid Input!!!!! \033[0m')

            for id in ids:
                url = baseurl + id
                if i >= maxp:
                    break
                i = i + 1
                try:
                    getData(url)
                except:
                    print('\033[91m Wrong ID!!!!! \033[0m')
        sys.exit(0)

    elif findMethod == '14':
        uids = findFolow.findFollow(1)
        for uid in uids:
            ids = findPID.findPIDs_by_Author(uid)
            savePath = basePath + uid

            isExists = os.path.exists(savePath)
            if not isExists:
                os.makedirs(savePath)
            os.chdir('%s' % savePath)

            i = 0

            maxp = int(input("Please enter the number of illustrations you need to download:"))
            if maxp >= len(ids):
                maxp = len(ids)
                print('Download All!')
            elif maxp <= 0:
                print('\033[91m Invalid Input!!!!! \033[0m')

            for id in ids:
                url = baseurl + id
                if i >= maxp:
                    break
                i = i + 1
                try:
                    getData(url)
                except:
                    print('\033[91m Wrong ID!!!!! \033[0m')
        sys.exit(0)

    elif findMethod == '15':
        uids = findFolow.findFollow(2)
        for uid in uids:
            ids = findPID.findPIDs_by_Author(uid)
            savePath = basePath + uid

            isExists = os.path.exists(savePath)
            if not isExists:
                os.makedirs(savePath)
            os.chdir('%s' % savePath)

            for id in ids:
                url = baseurl + id
                try:
                    getData(url)
                except:
                    print('\033[91m Wrong ID!!!!! \033[0m')
        sys.exit(0)

    elif findMethod == '16':
        uids = findFolow.findFollow(1)
        for uid in uids:
            ids = findPID.findPIDs_by_Author(uid)
            savePath = basePath + uid

            isExists = os.path.exists(savePath)
            if not isExists:
                os.makedirs(savePath)
            os.chdir('%s' % savePath)

            for id in ids:
                url = baseurl + id
                try:
                    getData(url)
                except:
                    print('\033[91m Wrong ID!!!!! \033[0m')
        sys.exit(0)

    elif findMethod == '17':
        illid = input('Please Enter illustration id:')
        ids = [illid]
        savePath = basePath
        isExists = os.path.exists(savePath)
        if not isExists:
            os.makedirs(savePath)
        os.chdir('%s' % savePath)
        for id in ids:
            url = baseurl + id
            try:
                getData_Overwrite(url)
            except:
                print('\033[91m Wrong ID!!!!! \033[0m')
        sys.exit(0)

    elif findMethod == '18':
        uids = findFolow.findFollow(2)
        for uid in uids:
            ids = findPID.findPIDs_by_Author(uid)
            savePath = basePath + uid

            isExists = os.path.exists(savePath)
            if not isExists:
                os.makedirs(savePath)
            os.chdir('%s' % savePath)

            for id in ids:
                url = baseurl + id
                old = 0
                try:
                    old = getData(url)
                except:
                    print('\033[91m Wrong ID!!!!! \033[0m')
                if old == 1:
                    print("\033[92m The author's illustrations are up to date \033[0m")
                    break
        sys.exit(0)

    elif findMethod == '19':
        uids = findFolow.findFollow(1)
        for uid in uids:
            ids = findPID.findPIDs_by_Author(uid)
            savePath = basePath + uid

            isExists = os.path.exists(savePath)
            if not isExists:
                os.makedirs(savePath)
            os.chdir('%s' % savePath)

            for id in ids:
                url = baseurl + id
                new = 0
                try:
                    new = getData(url)
                except:
                    print('\033[91m Wrong ID!!!!! \033[0m')
                if new == 1:
                    print("\033[92m The author's illustrations are up to date \033[0m")
                    break
        sys.exit(0)
    elif findMethod == '20':
        ids = findPID.findPIDs_by_Tag_sort()
        filename = ids[-1]
        ids.pop()
        savePath = basePath + filename + '_Tag'
        ids = list(set(ids))
        print(ids)
        method = input('Please enter the sort method:\n1.Like\n2.Bookmark\n3.View\n')
        if method == '1':
            idd = {}
            for id in ids:
                idd[id] = getInfo.GetLike(id)
            sortedList = sorted(idd, key=lambda x: x[1], reverse=True)
            print(sortedList)
        elif method == '2':
            idd = {}
            for id in ids:
                idd[id] = getInfo.GetBookmark(id)
            sortedList = sorted(idd, key=lambda x: x[1], reverse=True)
            print(sortedList)
        elif method == '3':
            idd = {}
            for id in ids:
                idd[id] = getInfo.GetView(id)
            sortedList = sorted(idd, key=lambda x: x[1], reverse=True)
            print(sortedList)
        else:
            print('\033[91m Invalid input!!!!! \033[0m')
            sys.exit(0)

        isExists = os.path.exists(savePath)
        print(savePath)
        print('isExist = %s', isExists)
        if not isExists:
            print('First time，new folder')
            os.makedirs(savePath)
            print('Create folder successfully')
        os.chdir('%s' % savePath)

        maxp = int(input("Please Enter number of illustrations you need to download:"))
        if maxp >= len(ids):
            maxp = len(ids)
            print('Download All!')
        elif maxp <= 0:
            print('\033[91m Invalid input!!!!! \033[0m')

        i = 0

        for id in sortedList:
            url = baseurl + id
            if i >= maxp:
                break
            i = i + 1
            try:
                getSortData(i, url)
            except:
                print('\033[91m Wrong ID!!!!! \033[0m')
        sys.exit(0)

    else:
        print('\033[91m Invalid Method!!!!! \033[0m')
        sys.exit(1)


    isExists = os.path.exists(savePath)
    print(savePath)
    print('isExist = %s',isExists)
    if not isExists:
        print('First time，new folder')
        os.makedirs(savePath)
        print('Create folder successfully')
    os.chdir('%s' %savePath)

    i = 0

    maxp = int(input("Please Enter number of illustrations you need to download:"))
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



    # id = '68151146'
    # url = baseurl + id
    # getData(url)

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


def getData(baseurl):  #获取数据并保存
    html = askURL(baseurl)
    #print(html)
    #soup = BeautifulSoup(html,'html.parser')
    html = str(html)
    #print(html)
    #print(re.findall(findP,html))
    #print(len(re.findall(findP,html)))
    #testlist = re.findall(findPage,html)
    #print(testlist)
    #print(html)
    pageList = re.findall(findP,html)
    #print(pageList)
    print('This illustration has %dp'%int(pageList[0]))



    url = str(re.findall(findUrl,html)[0])
    # title = str(re.findall(findName,html)[0])
    title = str(re.findall(findID,url)[0])
    print('pid = %s' %title)

    #R18 = re.findall(findR18, html)[0]
    #print("是否为R18:%s" %R18)

    #for page in range(0, 2):
    r = 0
    for page in range(0,int(pageList[0])):
        thisurl = url.replace('p0','p%d'%page)
        print('Visiting %s' %thisurl)


        try:
            try:
                type = re.findall(findType,thisurl)
                if os.path.exists('%s_p%d.%s' % (title, page, type[0])):
                    print('File already exists!')
                    r = 1
                    continue
                else:
                    img = advAskRes(thisurl)
                    print('Image format is %s' %type[0])
                    f = open('%s_p%d.%s' %(title,page,type[0]), 'wb')
                    f.write(img.read())
                    f.close()
                    print('\033[92m Save successfully\n \033[0m')
                    r = 0
            except:
                if url.find('ugoira0') != -1:
                    #print('此图片获取出现问题')
                    print('This image is gif，trying to save the static image\n')
                    #print(html)
                    #print(url)
                    #type = re.findall(findGifType,url)
                    type = ['jpg']
                    gifurl0 = url.replace('original','master')
                    #print(gifurl0)
                    gifurl1 = gifurl0.replace('png','jpg')
                    gifurl = gifurl1.replace('ugoira0','master1200')
                    #print(gifurl)
                    #type = ['jpg']
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

def getSortData(i, baseurl):  #获取数据并保存
    html = askURL(baseurl)
    #print(html)
    #soup = BeautifulSoup(html,'html.parser')
    html = str(html)
    #print(html)
    #print(re.findall(findP,html))
    #print(len(re.findall(findP,html)))
    #testlist = re.findall(findPage,html)
    #print(testlist)
    #print(html)
    pageList = re.findall(findP,html)
    #print(pageList)
    print('This illustration has %dp'%int(pageList[0]))



    url = str(re.findall(findUrl,html)[0])
    # title = str(re.findall(findName,html)[0])
    title = str(i) + '_' + str(re.findall(findID,url)[0])
    print('pid = %s' %title)

    #R18 = re.findall(findR18, html)[0]
    #print("是否为R18:%s" %R18)

    #for page in range(0, 2):
    r = 0
    for page in range(0,int(pageList[0])):
        thisurl = url.replace('p0','p%d'%page)
        print('Visiting %s' %thisurl)


        try:
            try:
                type = re.findall(findType,thisurl)
                if os.path.exists('%s_p%d.%s' % (title, page, type[0])):
                    print('File already exists!')
                    r = 1
                    continue
                else:
                    img = advAskRes(thisurl)
                    print('Image format is %s' %type[0])
                    f = open('%s_p%d.%s' %(title,page,type[0]), 'wb')
                    f.write(img.read())
                    f.close()
                    print('\033[92m Save successfully\n \033[0m')
                    r = 0
            except:
                if url.find('ugoira0') != -1:
                    #print('此图片获取出现问题')
                    print('This image is gif，trying to save the static image\n')
                    #print(html)
                    #print(url)
                    #type = re.findall(findGifType,url)
                    type = ['jpg']
                    gifurl0 = url.replace('original','master')
                    #print(gifurl0)
                    gifurl1 = gifurl0.replace('png','jpg')
                    gifurl = gifurl1.replace('ugoira0','master1200')
                    #print(gifurl)
                    #type = ['jpg']
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

def getData_Overwrite(baseurl):
    html = askURL(baseurl)
    #print(html)
    #soup = BeautifulSoup(html,'html.parser')
    html = str(html)
    #print(html)
    #print(re.findall(findP,html))
    #print(len(re.findall(findP,html)))
    pageList = re.findall(findP,html)
    #print(pageList)
    print('This illustration has %dp'%int(pageList[0]))



    url = str(re.findall(findUrl,html)[0])
    # title = re.findall(findName,html)[0]
    title = str(re.findall(findID, url)[0])
    print('pid = %s' % title)

    #R18 = re.findall(findR18, html)[0]
    #print("是否为R18:%s" %R18)


    for page in range(0,int(pageList[0])):
        thisurl = url.replace('p0','p%d'%page)
        print('Visiting %s' %thisurl)


        try:
            try:
                type = re.findall(findType,thisurl)
                img = advAskRes(thisurl)
                print('Image format is %s' %type[0])
                f = open('%s_p%d.%s' %(title,page,type[0]), 'wb')
                f.write(img.read())
                f.close()
                print('Save successfully\n')
            except:
                print('Something wrong')
                print('May be gif，trying to save the static image\n')
                type = re.findall(findGifType,url)
                #print(html)
                #print(url)
                gifurl0 = url.replace('original','master')
                #print(gifurl0)
                gifurl1 = gifurl0.replace('ugoira0.png','master1200.jpg')
                gifurl = gifurl1.replace('ugoira0','master1200')
                #print(gifurl)
                print('Image format is %s' % type[0])
                img = advAskRes(gifurl)
                f = open('%s_p%d.%s' % (title, page, type[0]), 'wb')
                f.write(img.read())
                f.close()
                print('Save successfully\n')
        except:
            print("It still doesn't work\n")

    print("Finish downloading\n")














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


if __name__ == "__main__":
    # 调用函数
    main()