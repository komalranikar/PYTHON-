def concatinate_dictionaries(B1,B2,B3):
  cse_dict = {}
  # write your code here
  cse_dict.update(B1)
  cse_dict.update(B2)
  cse_dict.update(B3)
  return cse_dict

B1 = {"110065001": "Ram", "110065002" : "Lakshman"}
B2 = {"120065001": "Bharat", "120065002" : "Satrugna"}
B3 = {"130065001": "Dhasaradh", "130065002" : "Babu"}
print(concatinate_dictionaries(B1,B2,B3))