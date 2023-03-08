# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def Ex(a):
    invert_lista = []
    my_num = str(a)
    lista = []
    for num in my_num:
        lista.append(int(num))
        for ss in lista:
            invert_lista = lista[::-1]
    if invert_lista == lista:
        print("Is palindrom")
    else:
        print("Not palindrom")


Ex(a)
