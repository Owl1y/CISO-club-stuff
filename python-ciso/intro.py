print("We are converting pounds to kilograms\n")

pounds = float(input("How many pounds would you like to convert?\n"))
kilograms = 0.45359

converted = pounds * kilograms

print(f'{pounds}lbs converted to kilograms is {converted}kg')

retry = input("Would you like to convert again? (y/n)\n").lower()

if retry in ('y', 'yes'):
    pounds = float(input("How many pounds would you like to convert?\n"))
    kilograms = 0.45359

    converted = pounds * kilograms

    print(f'{pounds}lbs converted to kilograms is {converted}kg')

