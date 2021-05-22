bill = int(input("What is the bill amount? $"))
people = int(input("How many people are splitting the bill? "))
tip = int(input("What % tip would you like to give? "))
tip_amount = bill * (tip/100)
share = round(((tip_amount+bill)/people),2)

print(f"Each person should pay ${share}")