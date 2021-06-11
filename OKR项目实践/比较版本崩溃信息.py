#! python3
# 匹配两个版本的崩溃信息，确认崩溃较早的引入版本.
import requests
from bs4 import BeautifulSoup
#获取单个版本崩溃排名前10的崩溃信息数组
def getTop10Details(version):#参数是需要获取崩溃信息的版本号，类似5192109
    #动态设置url网页链接
    url = 'http://172.20.205.59/index.php?selectVersion=' + version + '&Submit=%E6%90%9C%E7%B4%A2'
    #定义空数组，用来存储后续输入的崩溃信息数组
    results=[]
    res = requests.get(url)
    res.raise_for_status()
    bf = BeautifulSoup(res.text,'lxml')
    #按照tag<td class='single-line single-line-td'>条件来查找所有符合的崩溃信息
    textx=bf.find_all('td', class_= 'single-line single-line-td')
    # 循环输出崩溃排名前10的崩溃信息
    for i in range(0,9):
        results.append(textx[i].text)
    return(results)
#比较两个数组相同的元素，输出仅有相同元素的新数组
def Compare(resultx,resulty):
    resultz=[]
    for i in range(0,len(resultx)):
        for j in range(0,len(resulty)):
            if resultx[i]==resulty[j]:
                resultz.append(resultx[i])
    return resultz
#分行标号打印数组
def TypeArray(array):
    for i in range(0,len(array)):
        print(str(i+1)+' ' +array[i])
#输入函数需要查询对比的两个版本号参数信息
print("input the checking versions like '5192808' ")
version_a = input()
version_b = input()
print("ok,loading ")
TypeArray(Compare(getTop10Details(version_a),getTop10Details(version_b)))


