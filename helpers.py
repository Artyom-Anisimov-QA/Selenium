import random
from string import ascii_letters, digits

def generate_random_user():
    first_name = ''.join(random.choice(ascii_letters) for _ in range(9))
    last_name = ''.join(random.choice(ascii_letters) for _ in range(9))
    email = f'{first_name}.{last_name}@{random.choice(["gmail.com", "yandex.ru", "mail.ru"])}'
    password = ''.join(random.choice(ascii_letters + digits) for _ in range(10))

    return first_name, last_name, email, password

if __name__ == "__main__":
    print("Сгенерированный юзер")
    print(generate_random_user())