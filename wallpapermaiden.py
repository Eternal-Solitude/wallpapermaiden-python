import requests
from lxml import etree
for page in range(1,3):
    url='https://www.wallpapermaiden.com/category/anime?page='+str(page)
    print(url)
    header={
            "User-Agent": "Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3729.169Safari / 537.36"
        }
    r=requests.get(url,headers=header)
    r.encoding='utf-8'
    html=etree.HTML(r.text)
# 链接
    link=html.xpath("//div[@class='wallpaperBg']/a/@href")
# 分辨率
    ps=html.xpath("//div[@class='wallpaperBgRes wallpaperBgDefault']/text()")
# 名字
    title=html.xpath("//div[@class='wallpaperBg']/a/@title")
    for i in range(len(title)):
        print("\t\t'排名':'%d'," % (i + 1))
        print("\t\t'分辨率':'%s'," %ps[i])
        print("\t\t'关键词':'%s',"%title[i])
        linke=link[i]+'/download/'+ps[i]
        print(linke)


