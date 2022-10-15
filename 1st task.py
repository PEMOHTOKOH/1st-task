print("Який тип вашого рівняння або ви хочете згенерувати просте число? Уведіть відповідну цифру.")
print("1: a mod m = x \n"
      "2: a^b mod m = x \n"
      "3: a*x ≡ b mod m \n"
      "4: Згенерувати просте число. \n")
type_of_equation = int(input())

result = a = b = m = 1


def fast_power(a, b, m):
    nn = 0
    x = 1
    while nn < b:
        x = (x * a) % m
        nn += 1
    return x


def findNSD(a, m):
    if a == 0:
        return m
    while m != 0:
        if a > m:
            a = a - m
        else:
            m = m - a
    return a


def Resheto(a, b):
    c = [i for i in range(b + 1)]

    c[1] = 0
    i = 2
    while i <= b / 2:
        if c[i] != 0:
            j = i + i
            while j <= b:
                c[j] = 0
                j = j + i
        i = i + 1

    j = 0
    new_array_length = b - a + 1
    p = [0] * new_array_length

    while j < new_array_length:
        p[j] = c[j + a]
        j += 1

    p = set(p)
    # удаляем ноль
    p.remove(0)

    return p


match type_of_equation:
    case 1:
        print("Введіть а")
        a = int(input())
        print("Введіть m")
        m = int(input())

        x = a % m

        print("Результат: " + x)

    case 2:

        print("Введіть а")
        a = int(input())
        print("Введіть b")
        b = int(input())
        print("Введіть m")
        m = int(input())

        print("Результат: " + str(fast_power(a, b, m)))
    case 3:

        print("Введіть а")
        a = int(input())
        print("Введіть b")
        b = int(input())
        print("Введіть m")
        m = int(input())

        if findNSD(a, m) != 1:
            print("Знайти х неможливо, a та m не є взаємно простими")
        else:
            
            x = (b * fast_power(a, m-2, m)) % m

        print("Результат: " + str(x))
    case 4:

        print("Введіть а")
        a = int(input())
        print("Введіть b")
        b = int(input())
        print("Ось прості числа з заданого діапазону: " + str(Resheto(a, b)))

    case _:
        print("Введіть цифру")
