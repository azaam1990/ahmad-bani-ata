from tinydb import TinyDB,where
from tashaphyne.stemming import ArabicLightStemmer

ArListem = ArabicLightStemmer()
db = TinyDB('/json.json')
while True:
	x=input('Input to search or "q" to quit:\n>>> ')
	if x =='q':
		break
	ArListem.light_stem(x)
	x= ArListem.get_root()
	data = db.search(where('name').matches('.*%s.*'%x))
	for line in data:
		print(line['name']+': ',end='')
		print(line['value'])
		print()
	if not data:
		print('Not found result')
	
