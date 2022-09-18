k = 123
while k != 0:

    print("\nВведите число от 1 до 999999: \n"
          "Для выхода из программы введите 0")
    summa = input()
    ch = summa.isdigit()
    if ch == False:
        while ch == False:
            print("введите число от 1 до 999999 (цифрами)")
            summa = input()
            ch = str.isnumeric(summa)
    summa = int(summa)

    if summa == 0:
        break

    desatki1a = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    desatki1b = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    desatki2 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    desatki3 = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    desatki4 = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    desatki5 = ["тысяча", "тысячи", "тысяч"]
    desatki6 = ["рубль", "рубля", "рублей"]

    cifra1 = summa // 100000
    cifra2 = (summa // 10000) % 10
    cifra3 = (summa // 1000) % 10
    cifra4 = (summa // 100) % 10
    cifra5 = (summa // 10) % 10
    cifra6 = summa % 10

    slova = ""
    if cifra1 != 0:
        i1 = cifra1 - 1
        slova += desatki4[i1] + " "

    if cifra2 == 1 and cifra3 == 0:
        slova += desatki3[0] + " "
    if cifra2 != 1:
        if cifra2 != 0:
            i2 = cifra2 - 1
            slova += desatki3[i2] + " "

    if cifra3 != 0:
        if cifra2 == 1:
            i3 = cifra3 - 1
            slova += desatki2[i3] + " " + desatki5[2] + " "
        else:
            i3 = cifra3 - 1
            slova += desatki1b[i3] + " "
            if cifra3 == 1:
                slova += desatki5[0] + " "
            elif 1 < cifra3 < 5:
                slova += desatki5[1] + " "
            else:
                slova += desatki5[2] + " "
    if (cifra3 == 0) and (cifra2 or cifra1 != 0):
        slova += desatki5[2] + " "

    if cifra4 != 0:
        i4 = cifra4 - 1
        slova += desatki4[i4] + " "

    if cifra5 == 1 and cifra6 == 0:
        slova += desatki3[0] + " "
    if cifra5 != 1:
        if cifra5 != 0:
            i5 = cifra5 - 1
            slova += desatki3[i5] + " "

    if cifra6 != 0:
        if cifra5 == 1:
            i6 = cifra6 - 1
            slova += desatki2[i6] + " " + desatki6[2]
        else:
            i6 = cifra6 - 1
            slova += desatki1a[i6] + " "
            if cifra6 == 1:
                slova += desatki6[0] + " "
            elif 1 < cifra6 < 5:
                slova += desatki6[1] + " "
            else:
                slova += desatki6[2] + " "

    if (cifra6 == 0) and (cifra5 or cifra4 or cifra3 or cifra2 or cifra1 !=0):
        slova += desatki6[2]

    print(slova.capitalize())