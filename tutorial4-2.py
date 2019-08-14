x=input('Please enter some text: ')

try:
    type(int(x)) == int
    print('Woops! That\'s an integer, try again! ')
except:
    try:
        type(float(x)) == float
        print('Woops! That\'s a float, try again!')
    except:
        print(x)