def Ej(a,b):
    n = 0
    for i in range(a,b+1):
        for j in range(a,b+1):
            print(i * j, end="  ")
        print("\n")






print(Ej(2,100))