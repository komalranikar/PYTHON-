def capital_dict(d1):
  str_lst = []
  # write your code here
  a=list(d1.keys())   #taking all the keys from the dictionary in the form of list
  b=list(d1.values()) #taking all the values from the dictionary in the form of list
  for i in range(0,len(d1)):
    ele=a[i]+" -> "+b[i] #adding element in the form of "key -> value"
    str_lst.append(ele)  #appending the desired type of element in the str_lst
  return str_lst
d1 = {"J&K": "Srinagar", "Rajastan" : "Jaipur", "Gujarat" : "Gandhinagar" }
print(capital_dict(d1))