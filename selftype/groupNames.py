groupNames=[]
while True:
	print('Enter your group member name,member'+str(len(groupNames)+1)+'( or enter "end" to end your type):')
	memberName=input()
	if memberName=='end':
		print('you have stopped the enter')
		break
	groupNames=groupNames+[memberName]
print('Your group members are ')
for memberName in groupNames:
	print(''+memberName)