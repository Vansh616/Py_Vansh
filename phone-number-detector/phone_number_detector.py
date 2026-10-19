# This program checks if a given phone number is a possible mobile number in India, Australia, or New Zealand.


print(
    "Please enter a phone number to check if it is a possible mobile number in India, Australia, or New Zealand."
)

# Get user input for the phone number
while True:
    ph_num = input("Enter a phone number: ").strip()

    # Remove spaces and hyphens from the phone number
    ph_num = ph_num.replace(" ", "").replace("-", "")

    # Remove the country code if present
    if ph_num.startswith("+91"):
        ph_num = ph_num[3:]

    elif ph_num.startswith("+61"):
        ph_num = "0" + ph_num[3:]

    elif ph_num.startswith("+64"):
        ph_num = "0" + ph_num[3:]

    # Validate the input to ensure it is a valid phone number
    if not ph_num.isdigit():
        print("Invalid input. Only digits are allowed.")

    elif len(ph_num) <= 9:
        print("Invalid input. Phone number is too short.")

    else:
        break


# Check if the phone number is a possible mobile number in India, Australia, or New Zealand
def detect_phone_number(ph_num: int):

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
            "Number format not recognized. Please check the number and run the program again.",
            None,
        )


message, formatted_number = detect_phone_number(ph_num)
print(message)
if formatted_number:
    print(formatted_number)
