# If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the tip calculator!")

total_bill = int(input("What was the total bill?\n"))

bill_tip = int(input("How much would you like to tip?\n"))

people_amount = int(input("How many should split the bill?\n"))

tip_as_percent = bill_tip / 100
total_bill_tip = total_bill * tip_as_percent

total_bill = total_bill + total_bill_tip

bill_per_person = total_bill / people_amount

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
