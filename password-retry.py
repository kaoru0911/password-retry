password = 'a123456'
time = 3
while time > 0 :
	time = time - 1
	enter = input('請輸入密碼：')
	if enter == password :
		print('登入成功')
		break
	else:
		print('密碼錯誤')
		if time > 0:
			print('還有', time, '次機會')
		else:
			print('密碼錯誤三次，帳號已鎖定')




