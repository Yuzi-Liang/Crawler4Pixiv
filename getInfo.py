import urllib.request,urllib.error
import re

findFollow = re.compile(r'"total":(\d+?),')
findBookmark = re.compile(r'"bookmarkCount":(\d+?),')
findLike = re.compile(r'"likeCount":(\d+?),')
findView = re.compile(r'"viewCount":(\d+?),')


head = {
    'cookie': '__cfduid=d7b99ce8a7d81b42dd12e77246ff9ddc71614995990; first_visit_datetime_pc=2021-03-06+10:59:50; p_ab_id=6; p_ab_id_2=9; p_ab_d_id=655080259; yuid_b=g1OVQmA; __utmz=235335808.1614995995.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.954097025.1614995995; _gid=GA1.2.876905096.1614996006; PHPSESSID=14937409_Pb73USmrn8i9URonKIjQ0O9YGFu8CVrT; device_token=f37b0cc71b15e12e46a9328cc178b79b; c_type=29; privacy_policy_agreement=2; a_type=0; b_type=1; d_type=2; login_ever=yes; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=14937409=1^9=p_ab_id=6=1^10=p_ab_id_2=9=1^11=lang=zh=1; adr_id=vK0CqfVCtj9TKqZbyXv7GKFerDvT9EcqlvInvGHZYl9wQjwA; ki_r=; ki_s=214027:0.0.0.0.2; __gads=ID=ef30209119688eb0:T=1615019204:S=ALNI_MZSpSct-ZgilubdkoddtIhzqO1RPQ; __utma=235335808.954097025.1614995995.1615388458.1615439512.21; __utmc=235335808; OX_plg=pm; tag_view_ranking=0xsDLqCEW6~iFcW6hPGPU~RcahSSzeRf~EGefOqA6KB~Ie2c51_4Sp~RTJMXD26Ak~KN7uxuR89w~X_1kwTzaXt~qvqXJkzT2e~tgP8r-gOe_~Lt-oEicbBr~q3eUobDMJW~faHcYIP1U0~PHQDP-ccQD~_bee-JX46i~QaiOjmwQnI~zyKU3Q5L4C~at5kYG0Mvu~azESOjmQSV~nAtxkwJ5Sy~-StjcwdYwv~5oPIfUbtd6~LJo91uBPz4~_EOd7bsGyl~sr5scJlaNv~MkgAbGkXH6~L36Q8o7i1e~ePN3h1AXKX~Xyw8zvsyR4~FDuo9DrPoW~aLBjcKpvWL~ITqZ5UzdOC~skx_-I2o4Y~KhVXu5CuKx~CrFcrMFJzz~-sp-9oh8uv~qWFESUmfEs~bFoVVevmn4~B_OtVkMSZT~jH0uD88V6F~gpglyfLkWs~FH69TLSzdM~O2wfZxfonb~jk9IzfjZ6n~yqJYvivdJc~rsb55I7upx~MSNRmMUDgC~rOnsP2Q5UN~r43z9WTbmR~fIMPtFR8GH~1bmFwrp_zN~tEl-W_cZnm~AI_aJCDFn0~_hSAdpN9rx~j3leh4reoN~CBrKgQ-WQk~Z0p5mjlgxu~dCOVrVCqXA~4QveACRzn3~cofmB2mV_d~MM6RXH_rlN~mzJgaDwBF5~r9KLLtm3OI~rPzuYaLFlk~CLR9k9dHAQ~fRGJsS5rRM~Wzolb0OhOJ~BU9SQkS-zU~bXMh6mBhl8~Hjx7wJwsUT~CiSfl_AE0h~W8b5FozT7j~LVSDGaCAdn~G-44hwuIPi~D7ariL2KUO~EgWFYmVAdj~nDNbEmTVOG~0m_h2peuZi~6JhQxqtCvv~fKf7KbyaFa~GWOCnj3-NA~QqlTJrLZO5~oAnKp9i65M~QviSTvyfUE~2QTW_H5tVX~KOnmT1ndWG~04qbH3MKfd~ujS7cIBGO-~d2ro84lQRz~BQ41p36KLE~9OgM5t9f0L~skxn1VG9zl~RthHN5LPvq~a65-UMGqrO~SLphyXKNbQ~EUwzYuPRbU~c0C3o0MXIz~W4_X_Af3yY~Hvc3ekMyyh~1F9SMtTyiX; tags_sended=1; categorized_tags=AYsIPsa0jE~BU9SQkS-zU~CADCYLsad0~EGefOqA6KB~IVwLyT8B6k~NqnXOnazer~O2wfZxfonb~OEXgaiEbRa~PHQDP-ccQD~RcahSSzeRf~RsIQe1tAR0~_bee-JX46i~aLBjcKpvWL~b8b4-hqot7~bXMh6mBhl8~iFcW6hPGPU~kY01H5r3Pd~sr5scJlaNv; ki_t=1614996036137;1615439550234;1615440686226;9;402; __utmt=1; __utmb=235335808.17.10.1615439512; __cf_bm=0219269f55d735303ab7588a0d1bd586d714d0fe-1615441624-1800-AQjWKluA3ySvxWCHXSA/q7GjW9giTGpgdwCBQbFU9nItGsH7Z1/zY++rVFJk15FWrU3IsmPeUZdz2Ir78V1K35D527dnAtDI7AaZA3W/qLiV',
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

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        return 0

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
























urlShow = 'https://www.pixiv.net/ajax/user/14937409/following?offset=0&limit=24&rest=show&tag=&lang=zh'
urlHide = 'https://www.pixiv.net/ajax/user/14937409/following?offset=0&limit=24&rest=hide&tag=&lang=zh'




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