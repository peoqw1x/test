text = input("Введите текст: ")
start, end = map(int, input("Введите начало и конец через пробел: ").split())
print(text[start-1:end])