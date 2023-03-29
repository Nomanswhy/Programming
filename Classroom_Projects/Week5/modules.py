import random
import string
import time

random_number = random.randint(1, 10)
print(random_number)

letter = string.ascii_letters
print("Letters > ", letter)
digits = string.digits
print("Digits > ", digits)
symbols = string.punctuation
print("Symbols > ", symbols)

random_letter = random.choice(letter)
print('Random letter is > ', random_letter)
random_digit = random.choice(digits)
print("Random letter is > ", random_digit)
random_sign = random.choice(symbols)
print("Random letter is > ", random_sign)

cha_limit = 5
Magic_Word = ""
for character in range(cha_limit):
    Magic_Word += random.choice(digits+letter+symbols)
print("My word is > ", Magic_Word)

print("Messege will be displayed in 3 seconds...")
time.sleep(3)
print("3 seconds have passed...")

print("Processing...")

for i in range(10):
    time.sleep(1)
    print(f"\r{i*10+10}", end="")

print("\nComplete!")
