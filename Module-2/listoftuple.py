lst=[]
li=[]
n=int(input("number of elements you want to enter in list1:-"))
for i in range(0,n):
  ele=int(input())
  lst.append(ele)
for i in lst:
    l=(i,pow(i,2))
    li.append(l)
print(li)