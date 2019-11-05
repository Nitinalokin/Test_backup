a=[]
b=[]
with open("input2.txt") as f:
	for line in f:
		for i in line:
			a.append(i)
odd=open('odd.txt','w+')
even=open('even.txt','w+')

for i in a:
	if int(i)%2==0:
		even.write(i)
		even.write(' ')
	else:
		odd.write(i)
		odd.write(' ')

odd.close()
even.close()
