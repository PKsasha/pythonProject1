import random
random_number = random.randint(1, 10)
user_number = input("Угадай число:")

if user_number == random_number:
    print("Вы угадали")
else:
    print("Попробуйте еще раз")
    print(f"Bilo chislo {random_number}")
