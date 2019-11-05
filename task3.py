arr1=list(map(str,input().split()))
b=[]
for i in arr1:
	if i not in b:
		b.append(i)
print(b)		 