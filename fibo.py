
limit = int(input("Num"))
a = 0
b = 1
c = 0
for x in range(1,limit):
	c=a+b
	a=b
	b=c
	print(c)
	pass