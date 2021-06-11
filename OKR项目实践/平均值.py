import os
os.chdir("D:\\")
myFile = open("2kold.txt",encoding= 'utf-8')
myContent = myFile.readlines()
sumctm = 0
count = 0
for x in myContent:
    x=str(x)
    y = x.find('ms')
    ctms = x[y-4:y-3]
    ctmsy = x[y-6:y-5]
    ctmsz = x[y-7:y-6]
    if ctms =='_':
        ctm = x[y-3:-4]
        ctm = int(ctm)
        count=count+1
    else:平均值.py
        if ctmsy =='_':
            ctm = x[y-5:-4]
            ctm = int(ctm)
            count=count+1
        else:
            if ctmsz == '_':
                ctm = x[y-6:-4]
                ctm = int(ctm)
                count = count + 1
            else:
                ctm = x[y - 4:-4]
                ctm = int(ctm)
                count = count + 1
    sumctm = sumctm + ctm
    print(ctm)
print("sumctm = "+str(sumctm))
print("count = "+str(count))
print("averagy = "+str((sumctm/count)))


