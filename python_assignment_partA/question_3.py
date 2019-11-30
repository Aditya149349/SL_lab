def hourmin(num1):
    if (num1 == 60):
        print("1 hour 0 minutes")


    if(num1>60):
        while num1 > 60:
            c = (int)(num1 / 60)
            num1 = (int)(num1 % 60)

        print(c," hours and ",num1," minutes")
    else:
        print("0 hours and ",num1," minutes")





num2=int(input("enter the time : "))
hourmin(num2)
