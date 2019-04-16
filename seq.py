# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date  : 2019-04-16 16:29:21
# @Author: Garen Hou

import re
#把文件处理成单行
fr=open(r'C://Users//Administrator//Desktop//contigs.txt','r')
fw=open(r'C://Users//Administrator//Desktop//c1.txt','w') 
line=fr.read()
r=line.replace('\n','')
s=re.sub('>','\n>',r)
fw.write(s)
fr.close()
fw.close()

fr=open(r'C://Users//Administrator//Desktop//blastx_gp60_vs_contigs.txt','r')
fa=open(r'C://Users//Administrator//Desktop//c1.txt','r')#此处读取上面处理过的文件
fw_1=open(r'C://Users//Administrator//Desktop//2.txt','w')#写入
line_fr=fr.readlines()
line_fa=fa.readlines()
print(line_fa)
for eachline in line_fr:
	sp=eachline.strip().split('\t')
	#print(sp)
	title=sp[0]
	print(title)
	start=int(sp[7])
	#print(start)
	end=int(sp[6])
	#print(end)

	for each_seq in line_fa:
		#print(each_seq[:int(len(title)+2)].strip('ATGC'))
		if title == each_seq[:int(len(title))].strip('ATGC'):
			print(title+' 匹配成功')
			fw_1.write('>'+sp[0]+'\n'+each_seq[len(title)+int(start):len(title)+int(end)].strip()+'\n')
			
fr.close()
fa.close()
fw_1.close()