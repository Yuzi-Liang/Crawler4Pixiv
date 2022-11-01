import re
import urllib.request,urllib.error,urllib.parse
import gzip

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
        "cookie": "__cfduid=d7b99ce8a7d81b42dd12e77246ff9ddc71614995990; first_visit_datetime_pc=2021-03-06+10:59:50; p_ab_id=6; p_ab_id_2=9; p_ab_d_id=655080259; yuid_b=g1OVQmA; __utmz=235335808.1614995995.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=235335808; _ga=GA1.2.954097025.1614995995; _gid=GA1.2.876905096.1614996006; PHPSESSID=14937409_Pb73USmrn8i9URonKIjQ0O9YGFu8CVrT; device_token=f37b0cc71b15e12e46a9328cc178b79b; c_type=29; privacy_policy_agreement=2; a_type=0; b_type=1; d_type=2; login_ever=yes; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=14937409=1^9=p_ab_id=6=1^10=p_ab_id_2=9=1^11=lang=zh=1; adr_id=vK0CqfVCtj9TKqZbyXv7GKFerDvT9EcqlvInvGHZYl9wQjwA; OX_plg=pm; ki_r=; ki_s=214027:0.0.0.0.2; __gads=ID=ef30209119688eb0:T=1615019204:S=ALNI_MZSpSct-ZgilubdkoddtIhzqO1RPQ; categorized_tags=1DJe5jv-kK~2-ldUidl2y~7cMRrOPRjW~AYsIPsa0jE~CADCYLsad0~EGefOqA6KB~IVwLyT8B6k~NqnXOnazer~O2wfZxfonb~OT-C6ubi9i~PHQDP-ccQD~RcahSSzeRf~RkTaP3d-E6~b8b4-hqot7~iFcW6hPGPU~m9gg6bhnDE~sr5scJlaNv; tag_view_ranking=iFcW6hPGPU~EGefOqA6KB~0xsDLqCEW6~Yit50DXj_8~jlbI4zcRA-~xr1wAkJUyp~qvqXJkzT2e~_EOd7bsGyl~RTJMXD26Ak~sr5scJlaNv~PHQDP-ccQD~tgP8r-gOe_~Ie2c51_4Sp~Lt-oEicbBr~faHcYIP1U0~KN7uxuR89w~at5kYG0Mvu~RcahSSzeRf~FDuo9DrPoW~GNcgbuT3T-~qWFESUmfEs~LVSDGaCAdn~G-44hwuIPi~cbmDKjZf9z~5oPIfUbtd6~CrFcrMFJzz~D7ariL2KUO~EgWFYmVAdj~nDNbEmTVOG~0m_h2peuZi~6JhQxqtCvv~fKf7KbyaFa~GWOCnj3-NA~L-d833hYKU~dCOVrVCqXA~7cMRrOPRjW~_EEmAYVCDj~fBoUrsoPKp~2pqP3XcRN7~nrFOQYIh7z~y3NlVImyly~UpzWylGnYt~-cCD8382OO~wTJweG7Iqf~wyZOlBKxtg~FH69TLSzdM~TmJBC3K3bw~MM6RXH_rlN~bopfpc8En6~zyKU3Q5L4C~jH0uD88V6F~cofmB2mV_d~99-dVV-h9A~C9_ZtBtMWU~ouiK2OKQ-A~-sp-9oh8uv~_pwIgrV8TB~W8b5FozT7j~o4TRmIn06-~m9gg6bhnDE~gM8nSdLN-y~YI7Ufh1kvs~txZ9z5ByU7~UcTTPypj4n~ITqZ5UzdOC~KexWqtgzW1~2QTW_H5tVX~DosDk0jWon~q3eUobDMJW~ePN3h1AXKX~fRGJsS5rRM~Wzolb0OhOJ~suduYyiDRD~U06wIelPvJ~3Y00EEf2pf~2-ldUidl2y~v4ua7lr-1k~DjBjqF155l~5U2rd7nRim~4f-Z2cKZX7~CiHrWFfRgA~TWXAgOvqO3~bf55doAfAg~7xI6JRiT_O~Jotebt3yaa~Q9XCI2E9Gh~Hry6GxyqEm~GMhu-d9u9N~G_f4j5NH8i~AMwBN_-Fo_~ujS7cIBGO-~BU9SQkS-zU~y8GNntYHsi~c4Yb8OTkRv~wysb6V-bZi~_A694sY9oQ~qa-0isqPZy~bMWjDZvVht~xZ6jtQjaj9~w6HZJm4U_S; __utma=235335808.954097025.1614995995.1615008468.1615024882.3; __cf_bm=c1d3df66e2d7fb6d01c61bee5b398a28d209415a-1615031892-1800-AUTJ/LSgKyGMwRfu/mafkohyqd3I3nN6WE627IlXhJaul4pzbKFSkikci1IwJKfGiTcptcmmz7OInMaKNGnQSz0jw+trKbPLmJ3PuFd4gembNVksDCAWUV2d+IsiGnOakidFMSUEU99YLbm//Y+7Kgjj6knON9O2wNZdIDJkZLxKA8nItREmKXcgV3JHYMVRDA==; __utmt=1; ki_t=1614996036137;1614996036137;1615032396012;1;68; __utmb=235335808.12.10.1615024882",
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




# findPIDs_by_Author(4338012)
# findPIDs_by_Daily()
# findPIDs_by_Daily_R18()
# findPIDs_by_Weekly()
# findPIDs_by_Weekly_R18()
# findPIDs_by_Male()
# findPIDs_by_Male_R18()
# findPIDs_by_Female()
# findPIDs_by_Female_R18()
# findPIDs_by_Monthly()
# findPIDs_by_Tag()











