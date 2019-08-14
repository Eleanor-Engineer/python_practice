def Dem(name,age):
    if age == 30:
        return '{name} is 30!!!'.format(name=name)
    if age < 30 and age >= 0:
        return '{name} is {age} years old' .format (name = name, age = age )
    if age >30 and (type(age) == int or type(age) == float):
        return '{name} is at level {age}' .format (name = name, age = age )
    else:
        return  "Please enter a name first, then an age."

print(Dem('Hayley',22))
print(Dem('Sally',52))
print(Dem('Josh',30))