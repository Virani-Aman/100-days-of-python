for number in range(1, 11):
    print(number)
    
# range function is a function that can only be used in conjunction to some other function 
# It can be used to specify a range of numbers 
# It includes its starting number but not its ending one 
# so lets say you wanna add up numbers between 1-100 then you can use the function like this 

sum = 0 
for added in range(1, 101):
    sum += added
    
print(sum)