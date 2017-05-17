def longest_palindromic(text):
    arr = list(text)
    max = ""
    palindrome = []
    for i in arr:
        palindrome.append(i)
       if is_palindrome(str(text)):
           if len(max) < len(str(text)):
               max = str(text)

def is_palindrome(text):
    arr = list(text)
    reverse = arr[::-1]
    return arr == reverse

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
