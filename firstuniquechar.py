from operator import index


str =input()
c=0 
f=0
unique=""
for i in range(len(str)):
    c=0
    for j in range(len(str)):
        if str[i]==str[j]:
            c=c+1
    if c==1:
        #print(str[i])
         f=1
         unique=str[i]
         index =i
         break
if f==1:
    print("first unique char =",unique,"index =",index)
else:
    print(-1)