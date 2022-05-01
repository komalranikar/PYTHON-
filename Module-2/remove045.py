lst=[]
l=[]
n=int(input("number of elements you want to enter in a list:-"))
for i in range(0,n):
  ele=int(input())
  lst.append(ele)
for i in range(0,len(lst)):
  if i==0 or i==4 or i==5:
    lst.pop()
  else:
    l.append(lst[i])
print(l)

