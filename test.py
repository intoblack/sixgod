#coding=utf-8


#-*- coding:utf-8 -*-

import util


import re

class HtmlExtract(object):
	blocksWidth = 3
	remove_split = re.compile("\s+")
	pre_reg_list = [re.compile('(?is)<!DOCTYPE.*?>',re.I),re.compile("(?is)<!--.*?-->",re.I),re.compile('(?is)<script.*?>.*?</script>',re.I),re.compile("(?is)<style.*?>.*?</style>",re.I),re.compile("&.{2,5};|&#.{2,5};",re.I),re.compile('<!--.*?>'),re.compile("(?is)<.*?>",re.I)]
	# remove_enter = re.compile("\\n\\r")
	def __init__(self):
		pass



	def get_text(self,html):
		self.lineBlockDistribute([ i for i in self.pre_process(html.encode("utf-8")).split("\n")])
		

	def lineBlockDistribute(self,lines):
		indexDistribution = [ len(self.remove_split.sub("",i)) for i in lines]
		#取出上下两行空行文本
		for i in range(len(lines)-4):
			if lines[i] == 0 and lines[i+1] == 0 and lines[i+2] > 0 and lines[i+2] < 40 and lines[i+3] == 0 and lines[i + 4] == 0:
				lines[i+2] = ""
				indexDistribution[i+2] = 0
				i = i+ 1
				
		for i in range(len(lines)- self.blocksWidth):
			wordsum = indexDistribution[i]
			for j in range(i , i + self.blocksWidth):
				if j >= len(lines):
					break
				wordsum = wordsum + indexDistribution[j]
			indexDistribution[i] = wordsum
		return indexDistribution #返回块密度




	def pre_process(self,html):
		# self.remove_enter.sub("\\r",html) #python do match \n not best ,so i have to replace \r 
		for reg in self.pre_reg_list:
			html = reg.sub("",html)
		return html




# python 正则 . 除换行符任意一个字符


h = HtmlExtract()
html = util.get_url_data("http://finance.people.com.cn/n/2013/0914/c66323-22919783.html",codemode='gbk')
h.get_text(html)
# for h in h.split("\r"):
#     print h.encode("utf-8")
#     print "******************"