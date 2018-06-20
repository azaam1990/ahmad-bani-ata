import re,os

from tinydb import TinyDB, Query
dir_path = os.path.dirname(os.path.realpath(__file__))
db = TinyDB('/home/ahmd/Downloads/code/catg.json')
db.purge_tables()
f = open('/home/ahmd/Downloads/00.txt',encoding='utf-8')

catg = []
title = ''

xx=1
lis = []
for x in f:
	xx+=1
	print(xx)
	
	if re.match( r'\[\[تصنيف:.*\]\]', str(x)[:-1], re.M|re.I):

		s = str(x)[8:]
		match = re.match(r'^(\w|\s)*',s)

		if match:

			cat = str(match.group()).rstrip().lstrip()
			#text_file.write(cat+"\n")
			catg.append(cat)

	elif re.match( r'\s*\<title\>.*\<\/title\>\s*', str(x)[:-1], re.M|re.I):
		if title :
			lis.append({'title': title, 'catg': catg})
			catg = []

		title = str(x)[:-1].replace('<title>','').replace('</title>','').rstrip().lstrip()


db.insert_multiple(lis)
