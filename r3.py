lines = []
with open('3.txt', 'r', encoding= 'utf-8-sig') as f:
	
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	print(s)
	time_name = s[0]
	time = s[0][:5] # s[0]的前五個是時間 #字串也可以是清單，所以字串"13:32Allen"可視為清單，以清單分割
	name =s[0][5:]
	messege = s[1:]
	print(name)