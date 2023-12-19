bill = float(input("What was the total bill"))
tip = int(input("what would you like to tip? 10,12,15?"))
ppl = int(input("how many ppl split the bill"))

tipPercent = tip / 100 
tipAmount = bill * tipPercent
totalBill = bill + tipAmount
billPerPerson = totalBill / ppl
cost = round(billPerPerson, 2)


print(f"Each person should pay ${cost}")