def listReturn(spam):
    print("'")
    for i in spam:
        if spam.index(i)<(len(spam)-1):
            print(i+',')
        else:
            print('and '+i+"'")
spam=['cat','dog','ant','elephant']
listReturn(spam)