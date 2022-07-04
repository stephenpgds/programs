dis ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
str=input("enter the roman no")
prev=0
cur=0
res=0
for i in range (len(str)-1,-1,-1):
    cur=dis[str[i]]
    if (cur<prev):
        res-=cur
    else:
        res+=cur
    prev=cur
print(str,"roman to int",res)