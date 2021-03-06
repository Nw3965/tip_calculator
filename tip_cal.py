num = input ("What was the total bill? $")
people = input("How many people to split the bill?") 
num_as_int = int(num)
people_as_int = int(people)
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

bill = (num_as_int/people_as_int*(tip/100+1))
print (round(bill))
