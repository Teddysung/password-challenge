password = '1234'
chance = 3
ans = '1111'
while ans != password:
	ans = input('輸入密碼')
	if ans == password:
		print('登入成功')
		break
	chance = chance - 1
	print('登入失敗, 你還有', chance, '機會')
	if chance == 0:
		print('我要報警了, 再見!')
		break
