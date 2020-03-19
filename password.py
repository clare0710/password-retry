#密碼重試程式
#password = 'a123456'
#讓使用者重複輸入密碼
#最多輸入3次
#如果正確 就印出 "登入成功!"
#如果不正確 就印出 "密碼錯誤!" 還有_次機會!

password = 'a123456'
n = 3 # 剩餘機會
while True:
	p = input('請輸入密碼: ')
	if p == password:
		print('登入成功!')
		break # 逃出迴圈
	else:
		n = n - 1
		print('密碼錯誤! 還有',n,'次機會')
		if n == 0:
			break