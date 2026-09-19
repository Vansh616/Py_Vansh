# This program checks if a given phone number is a possible mobile number in India, Australia, or New Zealand.


print(
    "Please enter a phone number to check if it is a possible mobile number in India, Australia, or New Zealand."
)

# Loop until a valid phone number is entered
while True:
    # First input a phone number
    ph_num = input("Enter a phone number: ").strip()

    # Check if the phone number is valid (i.e., it should be at least 9 digits long and contain only digits)
    if len(ph_num) <= 9 or not ph_num.isdigit():
        print("Invalid input. Please enter a valid phone number: ")

    else:
        break


# Check if the phone number is a possible mobile number in India, Australia, or New Zealand
def detect_phone_number(ph_num):

    # Check for India
    if len(ph_num) == 10 and ph_num[0] in "6789":
        return "This number is a possible Indian mobile number.", "+91 " + ph_num

    # Check for Australia
    elif len(ph_num) == 10 and ph_num.startswith("04"):
        return "This number is a possible Australian mobile number.", "+61 " + ph_num[
            1:
        ]

    # Check for New Zealand
    elif len(ph_num) in (9, 10) and ph_num.startswith("02"):
        return "This number is a possible New Zealand mobile number.", "+64 " + ph_num[
            1:
        ]

    else:
        return (
            "Could not match this number with our countries currently supported.",
            None,
        )


message, formatted_number = detect_phone_number(ph_num)
print(message)
if formatted_number:
    print(formatted_number)
