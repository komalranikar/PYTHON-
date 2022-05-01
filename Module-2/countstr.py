def count(s, c) :
    res = 0
    for i in range(len(s)) :
        if (s[i] == c):
            res = res + 1
    return res
str=input()
c =input("enter the character you want to count:-")
print(count(str, c))
     