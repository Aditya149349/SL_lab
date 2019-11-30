def ChangeString(str1):
    str2 = ""
    str3 = ""
    i = 0
    for i in range(len(str1)):
        a = str1[i]
        if(a.isalpha()):
            char_num = chr(ord(a) + 1)
            str2 = str2 + str(char_num)
        else:
            str2=str2+a

    j = 0
    for j in range(len(str2)):
        b = str2[j]
        if b in 'aeiou':
            b = b.upper()

        str3 = str3 + b

    return str3


str1 = input("enter the string: ")
x = ChangeString(str1)
print(x)
