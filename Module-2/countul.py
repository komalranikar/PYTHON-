def string_test(s):
    upper=[]
    lower=[]
    for c in s:
        if c.isupper():
           upper.append(c)
        elif c.islower():
           lower.append(c)
        else:
           pass
    u=len(upper)
    l=len(lower)
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", u)
    print ("No. of Lower case Characters : ", l)
str=input()
string_test(str)