List=[(4,5),(4,),(5,3,4),(2,3)]
l=[]
k=int(input())
for i in List:
  if len(i)!=k:
    l.append(i)
print(l)