bill = float(input("What was the total bill? "))
tip_percent = float(input("What percentage tip would you like to leave? "))
ppl = int(input("How many people will split the bill? "))

tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / ppl
cost = round(bill_per_person, 2)

print(f"Each person should pay ${cost}")
