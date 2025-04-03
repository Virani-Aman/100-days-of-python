print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
tip =  input("How much % tip would you like to give? ")
people = input("How many people to split the bill? ")

bill =  int(bill)
tip =  int(tip)
people =  int(people)

 
final_bill  =  (bill + (bill * tip/100)) / people
print(f"each person should pay {final_bill}")
