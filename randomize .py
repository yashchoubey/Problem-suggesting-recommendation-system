#235000=205000+30000
from random import shuffle
with open('output.csv','r') as ip:
	data=ip.readlines()

header, rest=data[0], data[1:]

shuffle(rest)
print "step1"
with open('train.csv','w') as out:
	out.write(''.join([header]+rest[:205000]))
	
print "step2"
print "step1"
with open('test.csv','w') as out:
	out.write(''.join([header]+rest[205000:]))
