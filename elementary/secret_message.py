def checkio(words):
    counter = 0
    strs = words.split()
    for i in strs:
        if counter == 3:
            return True
        if not i.isalpha():
           counter = 0
        else:
            counter += 1
    return counter > 2


#  # These "asserts" using only for self-checking and not necessary for

# auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
