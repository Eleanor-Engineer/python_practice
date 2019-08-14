def funcWithArguments(x, y):
    
  if x == y:
    return "The numbers you entered are the same."
  elif x > y:
    return x
  else:
    return  y

print(funcWithArguments(6, 3))
print(funcWithArguments(34, 48))
print(funcWithArguments(123, 123))
