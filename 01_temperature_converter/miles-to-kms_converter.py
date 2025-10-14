# This is a  miles-to-kilometers converter

usr = input("Is it kilometers (kms) or miles (mi)? ")
distance = float(input("What's the distance? "))

if usr.lower() == "kms":
    d = distance / 1.609344
    unit = "miles"
    print(f"Converted distance is {d:.2f} {unit}")
elif usr.lower() == "m":
    d = distance * 1.609344
    unit = "kms"
    print(f"Converted distance is {d:.2f} {unit}")
else:
    print("Error: Invalid unit. Please use 'kms' or 'm'.")
