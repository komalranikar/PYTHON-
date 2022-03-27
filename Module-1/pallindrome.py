num=input("enter the variable to be checked:-")
i=0
for i in range(len(num)):
    if num[i]!=num[-1-i]:
        print(num,"is not a pallindrome")
        break
    else:
        print(num,"is a pallindrome")
        break

#output

'''
enter the variable to be checked:-22022
22022 is a pallindrome

'''