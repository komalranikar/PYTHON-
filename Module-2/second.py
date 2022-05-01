lst=[]
n=int(input("number of elements you want to enter in list:-"))
for i in range(0,n):
  ele=int(input())
  lst.append(ele)
lst.sort()
print("second largest number among the list is:-",lst[(len(lst)-2)])
print("second smallest number among the list is:-",lst[1])