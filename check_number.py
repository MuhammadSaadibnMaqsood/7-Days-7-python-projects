# # CHECK THE NUMBER


def check_number(num):
    if num % 2 == 0:
        return "even"

    return "odd"


print("\nWELCOME TO THE NUMBER CHECKER")
print("\nPRESS 0 for exit")

while True:
    input_num = input("Enter a number")
    convert = int(input_num)
    if convert == 0:
        break

    print("THE NUMBER IS ", check_number(convert))
