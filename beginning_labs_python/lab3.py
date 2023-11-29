def chesar(path_to_file, offset, language):
    if language.lower() in ["russian"] and 0 <= offset <= 32:
        dictionary_lower, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    elif language.lower() in ["english"] and 0 <= offset <= 25:
        dictionary_lower, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        print("Incorrect input data")
        return

    try:
        with open(path_to_file, 'r', encoding='utf-8') as file:
            file_text = file.read()
    except FileNotFoundError:
        print("File not found")
        return

    caesar_cipher = []

    for i in range(len(file_text)):
        if file_text[i] in dictionary_lower:
            dictionary = dictionary_lower
        elif file_text[i] in dictionary_upper:
            dictionary = dictionary_upper
        else:
            caesar_cipher.append(file_text[i])
            continue

        for j in range(len(dictionary)):
            if file_text[i] == dictionary[j]:
                if j + offset >= len(dictionary):
                    caesar_cipher.append(dictionary[(j + offset) % (len(dictionary))])
                elif 0 <= j + offset < len(dictionary):
                    caesar_cipher.append(dictionary[j + offset])

    with open("resources/result_file.txt", "w", encoding='utf-8') as file:
        print(''.join(caesar_cipher), file=file)

    result = ''
    for symbol in caesar_cipher:
        result += symbol

    return result


def main():
    # path_to_file = str(input("Enter path to file: "))
    # offset = int(input("Enter offset in number of symbols: "))
    # language = str(input("Enter language: "))

    chesar("resources/test_file.txt", 12, "russian")


main()
