def recall_password(cipher_grille, ciphered_password):
    elements_arr = []
    builder = ""
    for i in range(4):
        for i in enumerate(cipher_grille): # First rotate
            for char in enumerate(i[1]):
                if char[1] == "X":
                    builder += ciphered_password[i[0]][char[0]]
        cipher_grille = list(zip(*cipher_grille[::-1]))
    print elements_arr
    print builder
    return builder


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
