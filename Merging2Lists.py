def Ej(a, b):
    newList = []

    for num in a:
        if num % 2 !=0:
            newList.append(num)
    for num in b:
        if num % 2 ==0:
            newList.append(num)
    return newList


a = [1, 2, 3, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 99]

print(Ej(a,b))