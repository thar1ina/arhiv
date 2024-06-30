with open("all_characters.txt", "w") as file:
    # Добавляем буквы в нижнем регистре
    file.write(''.join(chr(i) for i in range(97, 123)))
    # Добавляем буквы в верхнем регистре
    file.write(''.join(chr(i) for i in range(65, 91)))
    # Добавляем цифры
    file.write(''.join(chr(i) for i in range(48, 58)))
    # Добавляем символы ASCII
    file.write('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
