import os
os.chdir("D:\\")
myFile = open("new 4.txt",encoding= 'utf-8')
myContent = myFile.readlines()
sumctm = 0
count = 0
for x in myContent:
    x=str(x)
    y = x.find('资产信息表中的每支股票的交易费用： ')
    ctms = x[y+18:-1]
    sumctm = sumctm+float(ctms)

    print(sumctm)



