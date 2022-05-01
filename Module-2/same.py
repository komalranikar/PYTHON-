def match_words(words):
  ctr = 0
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr
lst=[]
n=int(input("number of elements you want to enter in a list:-"))
for i in range(0,n):
  ele=input()
  lst.append(ele)
print(match_words(lst))