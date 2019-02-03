limit = int(input("ingrse limite"))
flag = 0
print(1)
print(2)
print(3)
for x in xrange(4,limit):
	flag=0
	for y in xrange(2,x-1):
		if(x%y==0):
			flag=flag+1
		pass
	if(flag==0):
		print(x)
	pass