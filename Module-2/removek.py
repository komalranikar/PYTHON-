List =  [(12, 13, 14), (14, 15), (16, 17), (18, 19)]
l=[]
k=int(input())
for i in List:
  if len(i)!=k:
    l.append(i)
print(l)