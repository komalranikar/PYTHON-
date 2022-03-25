even=[]
odd=[]
n=int(input("enter the number of range"))
for i in range(n):
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
print("total list of even number")
print(even)
print("total list of odd number")
print(odd)
evencount=len(even)
oddcount=len(odd)
print("total number of even numbers:-",evencount)
print("total number of odd numbers:-",oddcount)