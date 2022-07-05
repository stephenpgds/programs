res=input()
f=0
# for i in range(len(res)):
#     for j in range(i+1,len(res)):
#         if(res[i]==res[j]):
#             f=1
#             break
str=" ".join(sorted(res))
print(str)
if(f==0):
    print("unique")
else:
    print("not unique")
    