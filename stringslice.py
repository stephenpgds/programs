str=input("enter the string")
# for  i in range(0,len(str)-1,3):
#     print(str[i])
for i  in range(0,len(str)):
    print(str[:i])
for i  in range(len(str),0,-1):
    print(str[:i])
# print(str[:3])
# print(str[1:4])
# print(str[::-1])