# Lists

name = 'Hayley' # string str
level = 5 # integer int
awesomeness = 95.5 # float
is_raining = True # boolian bool
backpack = [] # list

backpack = [
    'drink bottle',
    'yoghurt',
    'headphones',
    'laptop'
]
#print(backpack)
backpack.append('blueberries')
#print(backpack)

#print(backpack[2])

backpack[1] = 'he he, this is a swap'
print(backpack)


for index,item in enumerate(backpack):   
    print(index, item)

counter = 0
while counter < len(backpack):
    print(counter, backpack[counter])
    counter= counter+1


numbers_list=(list(range(1,11,1)))
print(numbers_list)

#numbers = [1:10:1]
for number in numbers_list:
    print(number)


x=1
while x<11:
    print(x)
    x+=1

for num in range(1,11):
    print(num)

