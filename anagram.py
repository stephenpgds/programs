s=["eat","tea","tan","ate","nat","bat"]
dc={}
for i in s:
    w="".join(sorted(i))
    if w in dc:
        dc[w].append(i)
    else:
        dc[w]=[i]
# d=" ".join(list(dic))
# print(d)
print(tuple(dc.values()))