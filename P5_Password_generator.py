# scores = [155,122,133,44,22,11,111,200,222,199]
# max = 0
# for score in scores:
#     if score > max:
#         max = score
# print(max)
# sum = 0
# for number in range(1,101):
#     sum+=number
# print(sum)
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ''
for pw in range(1, nr_letters+1):
    password += random.choice(letters)
for pw in range(1, nr_symbols+1):
    password += str(random.choice(symbols))
for pw in range(1, nr_numbers+1):
    password += str(random.choice(numbers))
easy_pw = password
print(f"You easy password is : {easy_pw}")
pw_list = list(password)
random.shuffle(pw_list)
hard_pw = ''
for char in pw_list:
    hard_pw += char
print(f"Your hard password is : {hard_pw}")
