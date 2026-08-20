#PASSWORD GENERATOR

import random
import string

def gen_pass(length):
    characters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    
    password = ''.join(random.choice(characters + digits + special_characters) for _ in range(length))
    return password
    

print("WELLCOME TO PASSWORD GENERATOR")
print("---------------------------------")
length = input("Enter length: ")
converted = int(length)
password = gen_pass(converted)

print("\n\nHERE IS YOUR PASSWORD")
print(password)