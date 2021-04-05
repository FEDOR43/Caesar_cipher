# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print('Программа шифровки / дешифровки текста по методу Цезаря')
print('Нажмите "1" если требуется зашифровать сообщение, или "2", если требуется его дешифровать')
cipher = int(input())
print('Нажмите "1" если испульзуется кирилица, или "2", если используется латиница')
alphabet = input()
print('Укажите шаг сдвига (вправо)')
step = int(input())
if cipher == 2:
    step = - step
print('Введите текст для обработки')
text = input()

en_alphabet = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]
ru_alphabet = [chr(i) for i in range(1040, 1104)]


def cezar(text):
    if text[0] in en_alphabet:
        alphabet = en_alphabet;
        moch = 26
    else:
        alphabet = ru_alphabet;
        moch = 32
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                print(alphabet[(alphabet.index(text[i]) + step) % moch], end='')
            else:
                print(alphabet[(alphabet.index(text[i]) + step) % moch + moch], end='')
        else:
            print(text[i], end='')

cezar(text)
