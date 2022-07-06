s=input("enter the string")
r=input("enter the replace char")
res=""
for i in s:
    if i in "aeiouAEIOU":
        res=res+r
    else:
        res=res+i
print(res)
