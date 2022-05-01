lst1=[]
l=[]
n=int(input("number of elements you want to enter in list1:-"))
for i in range(0,n):
  ele=int(input())
  lst1.append(ele)
lst2=[]
n=int(input("number of elements you want to enter in list2:-"))
for i in range(0,n):
  ele=int(input())
  lst2.append(ele)
for i in range(0,5):
  diff=lst1[i]-lst2[i]
  l.append(diff)
print(l)