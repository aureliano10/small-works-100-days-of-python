#calculadora de propina
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10 12 15 "))

people = int(input("How many people to split the bill? "))

total = (bill * (tip / 100) + bill) / people

round_total = round(total, 2)
print(f"for person: {round_total}" )