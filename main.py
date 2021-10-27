'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    p = 1
    for i in lst:
        p = p * i
    return p


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
    while (x != y):
        if x > y:
            x = x - y
        if y > x:
            y = y - x

    return x


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
    r = 0
    while (x != 0):
        r = x % y
        y = x
        x = r
    return x


def main():
    while True:
        print("1. Determinati daca un nr. este prim")
        print("2. Determinati produsul numerelor dintr-o lista")
        print("3. Determinati cmmdc, varianta 1")
        print("4. Determinati cmmdc, varianta 2")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")
        if optiune == "1":
            x = int(input("Dati nr.:"))
            if is_prime(x):
                print("DA")
            else:
                print("NU")
        elif optiune == "2":
            x = int(input("Dati nr. de elemente:"))
            print("Dati elementele")
            list = []
            for i in range(0, x):
                list.append(int(input()))

            rezultat = get_product(list)
            print(rezultat)
        elif optiune == "3":
            print("Dati numerele")
            x = int(input())
            y = int(input())
            rezultat = get_cmmdc_v1(x, y)
            print(rezultat)
        elif optiune == "4":
            print("Dati numerele")
            x = int(input())
            y = int(input())
            rezultat = get_cmmdc_v2(x, y)
            print(rezultat)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")


if __name__ == '__main__':
    main()