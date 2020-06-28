#Реализовать программу шифрующую строку, задаваемую пользователем,
#с помощью алгоритма шифрования, использующего сдвиг на определенное
# количество знаков (шифр Цезаря). Сдвиг задается пользователем.


def ceasar_encode(letter, shift):
    if letter.isalpha():
        number = ord(letter) + shift % 25
        if number > 122 or 90 < number < 97:
            number -= 25
        return chr(number)
    return letter


i = 0
print('Введите текст')
text = input()
print('Введите сдвиг')
ii = int(input())
for line in text:
    i += ii
    for l in line:
        print(ceasar_encode(l, i), end='')

