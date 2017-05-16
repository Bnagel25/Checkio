def checkio(number):
    num_str = str(number)
    sum = 1
    for i in num_str:
        if not int(i) == 0:
            sum = sum * int(i)
    return sum


#  # These "asserts" using only for self-checking and not necessary for

# auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
