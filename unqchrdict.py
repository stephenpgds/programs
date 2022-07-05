str=input()
res={}
for i in str:
    if i in res:
        res[i]+1
    else:
        res[i]=1
for key,value in res.items():
    if value==1:
        print(key)
        #break

# for key,value in enumerate(str):
#     if res[value]==1:
#         print(value," ",key)
#         break