str1=input()
lower=[]
upper=[]
for char in str1:
    if char.islower():
        
        lower.append(char)
    else:
       
        upper.append(char)


sorted_str = ''.join(lower + upper)
print(sorted_str)