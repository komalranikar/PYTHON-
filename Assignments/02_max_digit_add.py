def add_maxdigit(nums):
  ans = []
  # write your code here
  a=max(nums)  #the mximum element of list
  b=str(a)     #converting it in string
  maxi=len(b)  #length of the number
  for i in nums:
    c=str(i)   #converting each element into string 
    if len(c)==maxi: #checking the length of each string and appending the elements which are of maximum length
      ans.append(i)
  return sum(ans)

nums = [122,23,345,2334,2344]
print(add_maxdigit(nums))