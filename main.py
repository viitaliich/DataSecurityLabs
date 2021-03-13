import time

# Таблиця 1 вертикального шифру Уітстона з ключовим словом ПРИКЛАД
matrix1 = [
    ['П', 'Р', 'И'],
    ['К', 'Л', 'А'],
    ['Д', 'Б', 'В'],
    ['Г', 'Ґ', 'Е'],
    ['Є', 'Ж', 'З'],
    ['І', 'Ї', 'Й'],
    ['М', 'Н', 'О'],
    ['С', 'Т', 'У'],
    ['Ф', 'Х', 'Ц'],
    ['Ч', 'Ш', 'Щ'],
    ['Ь', 'Ю', 'Я'],
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['0', '!', '.'],
    ['?', ',', ' '],
    ['\n', '_', '-']
]

# Таблиця 2 вертикального шифру Уітстона з ключовим словом КЛЮЧ
matrix2 = [
    ['К', 'Л', 'Ю'],
    ['Ч', 'А', 'Б'],
    ['В', 'Г', 'Ґ'],
    ['Д', 'Е', 'Є'],
    ['Ж', 'З', 'И'],
    ['І', 'Ї', 'Й'],
    ['М', 'Н', 'О'],
    ['П', 'Р', 'С'],
    ['Т', 'У', 'Ф'],
    ['Х', 'Ц', 'Ш'],
    ['Щ', 'Ь', 'Я'],
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['0', '!', '.'],
    ['?', ',', ' '],
    ['\n', '_', '-']
]


# Функція пошуку елементу в таблиці
def search(matrix, letter):
    i = 0
    index = tuple()
    while i < len(matrix):
        for j in range(len(matrix[i])):
            if matrix[i][j] == letter:
                index = (i, j)
                return index
        i = i + 1


def message_correction(message):
    message = message.upper()
    if len(message) % 2 != 0:
        message = message + ' '
    return message


def encrypt(message):
    translated = ""
    bigrams = list()
    i = 1
    while i < len(message):
        bigrams.append((message[i - 1], message[i]))
        i = i + 2

    for i in bigrams:
        first_sym = search(matrix1, i[0])
        second_sym = search(matrix2, i[1])
        first_sym_bi = (first_sym[0], second_sym[1])
        second_sym_bi = (second_sym[0], first_sym[1])
        translated = translated + matrix1[first_sym_bi[0]][first_sym_bi[1]]
        translated = translated + matrix2[second_sym_bi[0]][second_sym_bi[1]]

    return translated


def decrypt(message):
    translated = ""
    bigrams = list()
    i = 1
    while i < len(message):
        bigrams.append((message[i - 1], message[i]))
        i = i + 2
    for i in bigrams:
        first_sym = search(matrix1, i[0])
        second_sym = search(matrix2, i[1])
        first_sym_bi = (first_sym[0], second_sym[1])
        second_sym_bi = (second_sym[0], first_sym[1])
        translated = translated + matrix1[first_sym_bi[0]][first_sym_bi[1]]
        translated = translated + matrix2[second_sym_bi[0]][second_sym_bi[1]]

    return translated


def main():
    # Шифрування повідомлень
    message = "Український текст"
    message = message_correction(message)
    translated = encrypt(message)
    decrypted_message = decrypt(translated)

    print("MESSAGE: ", message)
    print("ENCRYPTED MESSAGE: ", translated)
    print("DECRYPTED MESSAGE: ", decrypted_message)

    # Шифрування файлів
    imputFilename = 'test_file.txt'
    ouputFilename = 'crypt_test_file.txt'
    fileObj = open(imputFilename, encoding='utf-8-sig')
    message = fileObj.read()
    fileObj.close()

    message = message_correction(message)

    # ------------------ Кодування з контролем часу -----------------
    StartTime = time.time()
    translated = encrypt(message)
    totalTime = (time.time() - StartTime)
    # -----------------------------------------------------------------------------
    outputfileObj = open(ouputFilename, 'w')
    outputfileObj.write(translated)  # Запис інформації у файл
    outputfileObj.close()

    print("FILE: ", message)
    print("ENCRYPTED FILE: ", translated)
    print('ENCRYPTION TIME: ', totalTime, 's')

    fileObj = open(ouputFilename)
    message = fileObj.read()
    fileObj.close()

    # ------------------ Декодування з контролем часу -----------------
    StartTime = time.time()
    translated = decrypt(message)
    totalTime = (time.time() - StartTime)

    print("DECRYPTED FILE: ", translated)
    print('DECRYPTION TIME: ', totalTime, 's')


main()
