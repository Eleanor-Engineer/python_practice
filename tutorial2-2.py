def funcWithArguments(x):
        
    if type(x) == int:

        if x == 5:
            return "The integer is exactly 5."
        else:
            return  x > 5
    else:
        return "Please enter an interger instead." 
print(funcWithArguments(10))
print(funcWithArguments(1))
print(funcWithArguments(5))
print(funcWithArguments(5.1))
