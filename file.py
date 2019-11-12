def atomic1():
    periodicTable = {
        'Na': 'SODIUM',
        'K': 'POTASSIUM',
        'Ca': 'CALCIUM'
    }
    key1 = input("enter the element symbol :\n")
    value1 = input("enter the name :")

    periodicTable[key1]=value1

    key2 = input("enter the element symbol :\n")
    value2 = input("enter the name :")

    periodicTable[key2] = value2

    print("the contents are :\n",periodicTable)

    print("the number of elements are :",len(periodicTable))

    key = input("enter the element you want to search ")
    print("the element is ",periodicTable[key])
