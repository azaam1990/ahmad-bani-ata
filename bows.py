from tinydb import TinyDB, Query
from tashaphyne.stemming import ArabicLightStemmer
import os

ArListem = ArabicLightStemmer()

dir_path = os.path.dirname(os.path.realpath(__file__))
sw = tuple(open('/home/ahmd/Downloads/python/stopword.txt').read().split())
text = open('/home/ahmd/Downloads/code/out.txt')
count = {}
xx = 1
for line in text:
    if xx == 1000000:
            break
    for word in line.split():
        print(xx)
        xx += 1	
        if xx == 1000000:
            break
        if not word in sw:
            ArListem.light_stem(word)
            count[ArListem.get_root()] = count.get(ArListem.get_root(), 0) + 1

lis = []
for key, value in count.items():
	lis.append({'name':key, 'value':value})
db = TinyDB('/home/ahmd/Downloads/code/bows.json')
db.purge_tables()
db.insert_multiple(lis)
