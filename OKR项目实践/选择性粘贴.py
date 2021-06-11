#拷贝对应条件的文件，从需要拷贝的文件夹，至对应文件夹，文件夹需提前创建
#导入函数库
import os
import shutil


#创建复制函数
def copyfile(fromwhere,towhere,filetype):
    #fromwhere是需要拷贝文件的原地址
    #towhere是需要拷贝至的目的地
    #filetype是需要拷贝的文件类型，类似“.txt”,“.log”,“.ini”这种
    for foldername, subfoldernames,filenames in os.walk(fromwhere):
        for filename in filenames:
            if filename.endswith(filetype):
                #遍历，如果文件名以filetype类型结尾，就处理文件
                abs= os.path.join(foldername,filename)
                #记录满足条件的文件对应绝对地址
                print('copy from '+abs)
                absx = abs.replace('\\','_')
                absy = absx.replace(':', '')
                #处理记录的绝对地址以供复制后重命名
                shutil.copy(abs, towhere+'\\' + absy)
                #复制文件至目的地后重命名，函数结束
print("Print the absolute address where you want to copy from,like 'D:\\111'")
fromwhere = input()
print("Then print the destination where you want to copy to,like 'D:\\111'")
towhere = input()
print("Finally,print the filetype you want to copy,like '.txt'")
filetype = input()
print("Ok! ")
copyfile(fromwhere,towhere,filetype)