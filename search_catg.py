from tinydb import TinyDB, Query,where
import os 
db = TinyDB( '/home/ahmd/Downloads/code/catg.json')
User = Query()
while True:
	x=input('Input to search or "q" to quit:\n>>> ')
	if x =='q':
		break
	data = db.search(where('title').matches('.*%s.*'%x))
	for line in data:
		print(line['title'])
		print(line['catg'])
		print()
	if not data:
		print('Not found result')
	
