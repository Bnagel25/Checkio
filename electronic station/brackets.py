def checkio(expression):
    left = []
    for i in expression:
        if i == "(" or i == "{" or i == "[":
            left.append(i)
        elif i == ")":
            if len(left) == 0 or left[-1] != '(':
                return False
            left.pop()
        elif i == "}":
            if len(left) == 0 or left[-1] != '{':
                return False
            left.pop()
        elif i == "]":
            if len(left) == 0 or left[-1] != '[':
                return False
            left.pop()
    if len(left) == 0:
            return True
    else:
            return False

#  # These "asserts" using only for self-checking and not necessary for

# auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
