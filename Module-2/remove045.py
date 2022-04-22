lst=["red","green","white","black","pink","yellow"]
l=[]
for i in range(0,len(lst)):
  if i==0 or i==4 or i==5:
    lst.pop()
  else:
    l.append(lst[i])
print(l)