
lines = []
with open('LINE.txt', 'r', encoding='utf-8') as f:
	for line in f:
		lines.append(line)

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print('時間: ', time)
	print(name)
