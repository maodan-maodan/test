
#加载主页，使用requests模块下载页面，使用beautiful soup找到页面中漫画图像的URL
#保存该页的漫画图片，利用iter——content（）系在漫画图像，并保存到硬盘
#转入前一张漫画的链接，然后重复
#重复直到第一张漫画

import bs4
import os
import requests

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    res = requests.get(url)
    print('Downloading image %s'%url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'lxml')
    soupFile = soup.select('#comic img')
    if soupFile==[]:
        print('null')
    else:
        downloadUrl = 'http:'+soupFile[0].get('src')
        print('Downloading image %s'%downloadUrl)
        res = requests.get(downloadUrl)
        res.raise_for_status()
        saveFile = open(os.path.join('xkcd',os.path.basename(downloadUrl)),'wb')
        for chunk in res.iter_content(100000):
            saveFile.write(chunk)
        saveFile.close()
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevLink.get('href')
print('Done')