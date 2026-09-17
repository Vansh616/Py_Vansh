# This program checks if a given phone number is a possible mobile number in India, Australia, or New Zealand.


print(
    "Please enter a phone number to check if it is a possible mobile number in India, Australia, or New Zealand."
)
while True:
    # First input a phone number
    ph_num = input("Enter a phone number: ").strip()

    # Check if the phone number is valid (i.e., it should be at least 9 digits long and contain only digits)
    if len(ph_num) < 9 or not ph_num.isdigit():
        print("Invalid input. Please enter a valid phone number: ")

    else:
        break


# if the phone number is valid, then check if it is a possible Indian mobile number
if len(ph_num) == 10 and ph_num[0] in "6789":
    print("This number is a possible Indian mobile number.")
    print("+91", ph_num)

# if the phone number is valid, then check if it is a possible Australian mobile number
elif len(ph_num) == 10 and ph_num.startswith("04"):
    print("This number is a possible Australian mobile number.")
    print("+61", ph_num[1:])

# if the phone number is valid, then check if it is a possible New Zealand mobile number
elif len(ph_num) in (9, 10) and ph_num.startswith("02"):
    print("This number is a possible New Zealand mobile number.")
    print("+64", ph_num[1:])

else:
    print("Could not match this number with our countries currently supported.")
