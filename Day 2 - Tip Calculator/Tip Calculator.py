print("Welcome to the Tip Calculator.")
bill = float(input("What was the total amount of your bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people are splitting the bill? "))
final_bill_per_person = (bill + bill * (tip / 100)) / split
print(f"Each person should pay: ${final_bill_per_person:.2f}")