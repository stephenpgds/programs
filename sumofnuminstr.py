def sum_of_num(s):
    num=0
    sum=0
    for i in s:
        if i.isdigit():
            num=num*10+int(i)
        else:
            sum=sum+num
            num=0
    return sum+num
s=input()
print(sum_of_num(s))