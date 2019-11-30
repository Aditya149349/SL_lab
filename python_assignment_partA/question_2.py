def lettersurround(str1):
    a=str1[0]
    if(a!="+"):
        print("false")
    else :
        str1=str1+' '

        for i in range(1, len(str1)):
            b=str1[i]
            c = str1[i + 1]
            if (b == "+"):
                if(c.isspace()):
                    print("true")
                    break
                continue
            if(b.isalpha()):

                if(c!="+"):
                    print("false")
                    break




            if(b.isalpha()== False):
                print("false")
                break


str2=input("enter the string: ")
lettersurround(str2)



