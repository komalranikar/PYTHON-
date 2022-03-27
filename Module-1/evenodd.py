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


#output
'''

enter the number of range100
total list of even number
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
total list of odd number
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
total number of even numbers:- 50
total number of odd numbers:- 50

'''