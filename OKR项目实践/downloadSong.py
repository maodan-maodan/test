
#加载主页，使用requests模块下载页面，使用beautiful soup找到页面中漫画图像的URL
#保存该页的漫画图片，利用iter——content（）系在漫画图像，并保存到硬盘
#转入前一张漫画的链接，然后重复
#重复直到第一张漫画

import bs4
import os
import requests

https://www.90pan.com/wap.php?action=space&pg=2&uid=0&folder_id=126076
url = 'https://www.90pan.com/wap.php'
os.makedirs('Jachou',exist_ok=True)
params = {
    "action":"space",
    "folder_id":"126076"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36"
}

res = requests.get(url,params=params,headers=headers)
# print('Downloading song %s'%url)
results = res.content.decode('utf-8')
soup = bs4.BeautifulSoup(results,'lxml')
print(soup)
soupFile = soup.select('.item f16 color1 a')
if soupFile==[]:
    print('null')
else:
    downloadUrl = 'http:'+soupFile[0].get('href')
    print('Downloading song %s'%downloadUrl)
    res = requests.get(downloadUrl)
    res.raise_for_status()
    saveFile = open(os.path.join('Jachou',os.path.basename(downloadUrl)),'wb')
    for chunk in res.iter_content(100000):
        saveFile.write(chunk)
    saveFile.close()
# prevLink = soup.select('a[rel="prev"]')[0]
# url = 'http://xkcd.com'+prevLink.get('href')
# print('Done')