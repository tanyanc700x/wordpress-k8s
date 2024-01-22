import random
import string

def generate_password(length=14):
    # Символы, что будут юзаться для генерации пароля
    characters = string.ascii_letters + string.digits + string.punctuation

    # Собсна генерация пароля
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Создание пароля длиной 14 символов
password = generate_password()
print(password)