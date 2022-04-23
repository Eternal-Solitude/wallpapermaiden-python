from bs4 import BeautifulSoup
import requests
from lxml import etree
import time
import random

for page in range(1,1040):#1040改成自己的想要爬取多少页数
    url='https://www.wallpapermaiden.com/category/anime?page='+str(page)
    print(url)
    ua = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.123 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.123 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.70 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.123 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",]
    r=requests.get(url,headers={"user-agent":random.choice(ua)})#,proxies=proxy)
    r.encoding='utf-8'
    html=etree.HTML(r.text)
# 链接
    link=html.xpath("//div[@class='wallpaperBg']/a/@href")
# 分辨率
    ps=html.xpath("//div[@class='wallpaperBgRes wallpaperBgDefault']/text()")
# 名字
    title=html.xpath("//div[@class='wallpaperBg']/a/@title")

    

    for i in range(len(title)):
        linke=link[i]+'/download/'+ps[i]

        img_herf = requests.get(linke,headers={"user-agent":random.choice(ua)})#,proxies=proxy)
        img_herf_Bs = BeautifulSoup(img_herf.text,"html.parser")
        alist = img_herf_Bs.find("div",class_="wallpaperPreviewContent").find("div",class_="wpPreviewSection").find("div",class_="wpBig wpBigFull").find_all("a")

        for a in alist:
            img_url = (a.get("href"))

            img_url_get = requests.get(img_url,headers={"user-agent":random.choice(ua)})#,proxies=proxy)
            img_name = img_url.split("/")[-1]
            with open("img/"+img_name,mode="wb") as f:
                f.write(img_url_get.content)   
        print("over!!",img_name)
        time.sleep(1)

print("over!!"+url)
time.sleep(5)