# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date  : 2018-11-22 13:03:22
# @Author: Garen Hou
# GAREN'S PRACTICE DRAFT
# 10000 HRs

import requests
import re
import os
basicUrl=''#注意这里不能用ftp://开头，要改成http://

def getHTMLText(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""

html = getHTMLText(basicUrl)
r= re.compile(r'\w*.pdf')
for filename in r.findall(html):#找到pdf文件 或其他格式
    if not os.path.exists(filename):#若该文件之前没有保存过，则保存下来
        with open(filename, 'wb') as f:
            file=requests.get(basicUrl+filename)
            f.write(file.content) #保存文件用二进制形式