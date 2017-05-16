def checkio(data):

    # replace this for solution
    builder = ""
    while data > 0:
        if data >= 1000:
            builder += "M"
            data -= 1000
        elif data >= 900:
            builder += "CM"
            data -= 900
        elif data >= 500:
            builder += "D"
            data -= 500
        elif data >= 400:
            builder += "CD"
            data -= 400
        elif data >= 100:
            builder += "C"
            data -= 100
        elif data >= 90:
            builder += "XC"
            data -= 90
        elif data >= 50:
            builder += "L"
            data -= 50
        elif data >= 40:
            builder += "XL"
            data -= 40
        elif data >= 10:
            builder += "X"
            data -= 10
        elif data >= 9:
            builder += "IX"
            data -= 500
        elif data >= 5:
            builder += "V"
            data -= 5
        elif data >= 4:
            builder += "IV"
            data -= 4
        elif data >= 1:
            builder += "I"
            data -= 1
        print builder
    return builder


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
