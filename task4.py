a = {"a":"A","b":"B","c":[2,4,6,{"a":"A","b":"B"}],"d":{"a":[2,4,6],"b":[5,2,1]}}		
			
ch1='a'
ch2='z'

ch3=2
ch4=0


def arr(a):
	if isinstance(a,list):
		c=[]
		for i in a:
			c.append(arr(i))
		return c
	elif isinstance(a,dict):
		d = {}
		for x,y in a.items():
			d.update({arr(x):arr(y)})
		return d
	else:
		if a==ch1:
			return ch2
		elif a==ch3:
			return ch4	
	return a

print (a)
newlist=arr(a)
print (newlist)

