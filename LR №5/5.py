import random
import string
def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    random_string = ''

    for i in range(length):
        random_string += random.choice(characters)

    return random_string
message = input("Введите сообщение: ")
n = int(input("Введите количество символов: "))
new_message = ""
for letter in message:
    new_message += letter
    new_message += generate_random_string(n)
print("Закодированное сообщение:", new_message)