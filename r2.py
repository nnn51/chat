# 讀取檔案
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding= 'utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat		

# 轉換檔案
def convert_file(lines):
	sum_allen = 0
	sum_viki = 0
	sum_allen_p = 0
	sum_allen_s = 0
	sum_viki_p = 0
	sum_viki_s = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '圖片':
				sum_allen_p += 1
			elif s[2] == '貼圖':
				sum_allen_s += 1	
			else:	
				for m in s[2:]:
					sum_allen = len(m) + sum_allen
		elif name == 'Viki':
			if s[2] == '圖片':
				sum_viki_p += 1
			elif s[2] == '貼圖':
				sum_viki_s += 1	
			else:
				for m in line[2:]:
					sum_viki = len(m) + sum_viki	

	print('Allen共打了', sum_allen, '個字，傳了', sum_allen_p, '張圖片跟', sum_allen_s, '張貼圖')
	print('Viki共打了', sum_viki, '個字，傳了', sum_viki_p, '張圖片跟', sum_viki_s, '張貼圖')


# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding= 'utf-8-sig') as f:  
		for line in lines:
			f.write(line)	

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert_file(lines)
	# write_file('output.txt', lines )

main()
