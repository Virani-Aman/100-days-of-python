fruits = ["apple", "PEAR", "Pineapple"]

for fruit in fruits:
    print(fruit)
    
# So a for loop is used like this 
# What is happening is basically the for loop makes fruit a variable and then takes out the 1st/0 word or the data in the list and then puts the value of fruit to that 
# and then does the print task and this process keeps repeating till each one of the data in the list was passed through it ]

# For example lets use it to find the total score 
# Lets say you have a list of numbers that you need to add 

numbers = [111111, 111111, 2324234, 123123, 324234, 8709, 9999, 28282]

sum = 0
for number in numbers:
    sum += number    
print(number)


# Lets say you wanna loop through and find the biggest number then 
# We can use the for loop like this 

max_number = 0
for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)
 