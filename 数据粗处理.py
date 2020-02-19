# By Bing_Yanchi
import csv

data = []
after = []

# 读取数据
def read():
	with open('DXYArea.csv',encoding='utf-8') as f:
		f_csv = csv.reader(f)
		for row in f_csv:
			del row[13],row[12],row[11],row[10],row[9],row[8],row[7],row[5],row[4],row[3],row[2],row[1]
			data.append(row)

# 合并数据
def merge():
	for i in range(len(data)):
		if i > 0 :
			if data[i][0] != data[i-1][0]:
				if data[i][2] != data[i-1][2]:
					data[i][2] = data[i][2][:-4]
					after.append(data[i])
# 添加表头
def reverse():
	after.reverse()
	after.insert(0,['name','value','date'])

# 写出数据
def write():
	with open('data.csv','w',newline='',encoding='utf-8') as f:
		f_csv = csv.writer(f)
		for row in after:
			f_csv.writerow(row)

read()
merge()
reverse()
write()