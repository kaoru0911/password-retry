password = 'a123456'
time = 3
while time > 0 :
	enter = input('請輸入密碼：')
	if enter == password :
		print('登入成功')
		break #逃出迴圈
	else:
		print('密碼錯誤，還有', time - 1, '次機會')
		time = time - 1




