# coding: UTF-8
import requests
from bs4 import BeautifulSoup
import numpy as np 
import pandas as pd
import socket
import time


def get_pages(d,file_op):
	years = range(2007,2018)
	months = range(1,13)
	socket.setdefaulttimeout(20)
	for year in years:
		for month in months:
			tmp_list = []
			link = "http://www.creprice.cn/rank/capitallease.html?type=22&y="+ str(year) +"&m=" + str(month)
			print("The link is "+ link)
			headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
						'Host':'www.creprice.cn'
					}

			r = requests.get(link,headers=headers,timeout=100)
			print("响应码：",r.status_code)
			soup = BeautifulSoup(r.text.replace(u'\xa9',u''))
			tr_list = soup.find_all('td')
			file_op.write(str(year)+"年"+str(month)+"月"+'\n')
			for each in tr_list:
				name = each.text.strip()
				tmp_list.append(name)
			for i in range(0,len(tmp_list)):
				if (i%6 == 1):
					if i%6 == 1:
						if (tmp_list[i]) not in d:
							d[tmp_list[i]]= {}
						
						if str(year) not in d[tmp_list[i]]:
							d[tmp_list[i]][str(year)] =[None] * 12
							
						if tmp_list[i+2] != '--':
							d[tmp_list[i]][str(year)][month - 1] = (float(tmp_list[i+2].replace(',','')))


			r.close()
			time.sleep(1)

with open('1.txt','w') as f:
	dict = {}
	name_list = []
	get_pages(dict,f)
#	for i in range(2017,2018):
#		print(dict['北京'][str(i)])
#	f.write(name_list)
#	for i in range(0,len(name_list)):
#		if i%6 == 1 or i%6 == 3:
#			f.write(name_list[i]+'\n')

#for i in dict:
#	for j in dict[i]:
#		if len(dict[i][j])!=0:
#			dict[i][j] = float(sum(dict[i][j]) / len(dict[i][j]))

import csv

with open('租商铺面板.csv','w') as Csv_op:
	w = csv.writer(Csv_op)
	head = []
	for y in range(2007,2017):
		for m in range(1, 13):
			head.append(str(y) + '年' + str(m) + '月')
	w.writerow(head)
	w.writerows(dict.items())
