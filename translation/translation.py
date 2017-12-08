#-*- coding: UTF-8 -*- 
import uniout
import codecs
import collections




with codecs.open('./bi-weekly-1207.md',encoding='utf-8') as f:
	with codecs.open('./bi-weekly-1207_tc.md',"w",encoding='utf-8') as g:
		content=f.read()
		#print content
		#content.encode('utf-8')
		#print content.find('\xe9')
		#print content[31:40]

		replace_dic={ u'西部數據':u'WD',u'西部資料':u'WD', u'巴塞羅那':u'Barcelona' , u'超算中心': u'BSC-CNS(Barcelona Supercomputing Center', u'數據':u'資料', u'采':u'採', u'福布斯':u'Forbes', u'官文':u'官方新聞', u'工作組':'workgroup',u'內存訪問':u'memory access' , u'關系':u'關係',u'擴展':u'extension', u'安全':u'Security', u'仿真': u'Simulation',u'物理設計':u'physical design',u'內存模型':u'memory model',u'體系結構':u'Architecture' ,u'葉子節點':u'leaf node ',u'標志位':u'flag', u'硬件控制':u'HW control',u'頁表':u'page table ', u'硬件':u'硬體',u'軟件':u'軟體', u'模塊':u'module ',u'帶寬':'bandwidth', u'項':'entry', u'軟件緩存':u'software cache '}
		for i in replace_dic:
			print i
			print replace_dic[i]
			content=content.replace(i, replace_dic[i])
		g.write(content)

