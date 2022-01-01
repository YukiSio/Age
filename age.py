driving = input('請問你有沒有開過車（有／沒有）：')
age = input('請問你的年齡：')
if driving == '有':
	if int(age) >= 18:
		print('你通過測驗了')
	else:
		print('奇怪，你怎麼會開過車')
elif driving =='沒有':
	if int(age) >= 18:
		print('你可以去考駕照啦')
	else:
		print('再過幾年就可以去考駕照啦')
else:
	print('只能輸入有或沒有')