# Concept : Dictionaries
# concat dictionaries
'''
You will be given three dictionaries, representing three sections -- containing rollnumber and corresponding Names

B1 = {"110065001": "Ram", "110065002" : "Lakshman"}
B2 = {"120065001": "Bharat", "120065002" : "Satrugna"}
B3 = {"130065001": "Dhasaradh", "130065002" : "Babu"}

Each dictionary representing a particular section.

Now if we want to get all the students from the branch CSE, you have to mix all dictionaries and present a single Dictionary with all the roll numbers and students.

Your task is to combine the given dictionaries into cse_dict and return the cse_dict

Take a hint to use update() function
'''
import unittest

def concatinate_dictionaries(B1,B2,B3):
  cse_dict = {}
  # write your code here
  cse_dict.update(B1)
  cse_dict.update(B2)
  cse_dict.update(B3)
  return cse_dict


# DO NOT TOUCH THE BELOW CODE

class Concatination(unittest.TestCase):
  def test_01(self):
    B1 = {"110065001": "Ram", "110065002" : "Lakshman"}
    B2 = {"120065001": "Bharat", "120065002" : "Satrugna"}
    B3 = {"130065001": "Dhasaradh", "130065002" : "Babu"}
    output = {"110065001": "Ram", "110065002" : "Lakshman", "120065001": "Bharat", "120065002" : "Satrugna", "130065001": "Dhasaradh", "130065002" : "Babu"}
    
    self.assertEqual(concatinate_dictionaries(B1,B2,B3), output)

  def test_02(self):
    B1 = {"110065001": "shyam", "110065002" : "sundar"}
    B2 = {"120065001": "satyam", "120065002" : "sivam"}
    B3 = {"130065001": "ved", "130065002" : "stalon"}
    output = {"110065001": "shyam", "110065002" : "sundar", "120065001": "satyam", "120065002" : "sivam", "130065001": "ved", "130065002" : "stalon"}
    
    self.assertEqual(concatinate_dictionaries(B1,B2,B3), output)

if __name__ == '__main__':
  unittest.main(verbosity=2)