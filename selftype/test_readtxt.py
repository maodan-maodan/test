import os
filename = os.path("D:\\1.txt")

with open(filename) as notTmp:
    lines = notTmp.readlines()

print_string = ''
for line in lines:
    print_string = print_string+line.rstrip()

print(print_string)