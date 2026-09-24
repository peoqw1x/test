text = input("Введите текст: ")
find = input("Введите слово для поиска: ")
if find in text:
    char_num = text.count(find)
    print(f"Слово '{find}' встречается в тексте {char_num} раз")
char_num = len(text)
print(f"Количество символов в тексте: {char_num}")
print("Изменённый текст:", text.replace(find, ""))