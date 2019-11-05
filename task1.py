arr=[]
word=""
with open("input.txt") as fileobj:
    for line in fileobj:  
    	for ch in line:
    		if ch!=" " and ch!=".":
    			word+=ch
    		elif ch==".":
    			arr.append(word)
    			word=""
    		else:		
    			arr.append(word)
    			word=""
    	if word!="":
    		arr.append(word)
print(arr)
d={}
for i in arr:
	if i in d:
		d[i]+=1
	else:
		d[i]=1
print(d)			   		

           