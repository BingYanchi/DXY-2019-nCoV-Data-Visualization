# By Bing_Yanchi
import csv

time = []
final = []
province = ['北京市','广东省','山东省','江苏省','河南省','上海市','河北省','浙江省','陕西省','湖南省','重庆市','福建省','天津市','云南省','四川省','广西壮族自治区','安徽省','海南省','江西省','湖北省','山西省','辽宁省','黑龙江','内蒙古自治区','贵州省','甘肃省','青海省','新疆维吾尔自治区','西藏区','吉林省','宁夏回族自治区']
value = {}
mid = []

# 生成字典
def init():
	for i in range(len(province)):
		value[province[i]] = '0'

# 获取时间列表
def get_time():
	with open('data.csv',encoding='utf-8') as f:
		f_csv = csv.reader(f)
		for row in f_csv:
			time.append(row[2])
		del time[0]

# 主程序
def main():
	with open('data.csv',encoding='utf-8') as f:
		f_csv = csv.reader(f)
		for row in f_csv:
			if row[2] != 'date':
				value[row[0]] = row[1]
				for a in range(len(province)):
					final.append([province[a],value[province[a]],row[2]])
	final.insert(0,['name','value','date'])

# 写出数据
def write():
	with open('data_new.csv','w',newline='',encoding='utf-8') as f:
		f_csv = csv.writer(f)
		for row in final:
			f_csv.writerow(row)

init()
main()
write()