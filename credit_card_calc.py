
def check_gtin13_input(x):
    if len(str(x)) > 13 or len(str(x)) < 12:
        return 'Please enter a number with 12 or 13 digits.'
    elif str.isdigit(str(x)):
        return 'OK'
    else:
        return'Oops, looks like you entered some characters which aren\'t digits.'
        


def gtin13_calc(x):
    if check_gtin13_input(x) is not 'OK':
        #stop the function
        return check_gtin13_input(x)

    # convert input to a list.
    x=[int(a) for a in str(x)]

    # Define variables for while loop
    sum = 0
    a=0
    # Do the loop for all the didgets, excludinmg the check digit.
    while a < 12:
        # This method of checks is taken from https://en.wikipedia.org/wiki/Luhn_algorithm
        # 1) From the rightmost digit, which is the check digit, and moving left, double the value of every second digit. The check digit is not doubled; the first digit doubled is immediately to the left of the check digit. If the result of this doubling operation is greater than 9 (e.g., 8 × 2 = 16), then add the digits of the result (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or, alternatively, the same final result can be found by subtracting 9 from that result (e.g., 16: 16 − 9 = 7, 18: 18 − 9 = 9).
        adding= (2*(a % 2)+1)*x[a]
        sum += adding
        a = a + 1
    
    check_no_calc = -sum % 10
        

        
    #See if the check number was entered in by the user.  If so, tell them if the number is valid.
    if len(x)  == 13:
        check_no_entered = int(x[12])    
        if  check_no_entered == check_no_calc:
            return 'This is a valid gtin13 barcode.'
        else:
            return 'This is NOT a valid gtin13 barcode.'
    else:
        return check_no_calc


# create function of the same names has Hayley's
def validate_gtin13_barcode_check_digit(x):
    message = gtin13_calc(x)
    return message
def calculate_gtin13_barcode_check_digit(x):
    return gtin13_calc(x)

# Other checks for the code with the other function names
#This was to check by check funciton, lols.
#print(check_gtin13_input(1234567890987))
#print(check_gtin13_input('a'))
#print(check_gtin13_input('12d333333333'))

#Required to give 5
#print(gtin13_calc('940055061977'))

#Required to report is a valid GTIN 13 Barcode.
#print(gtin13_calc('9781861972712'))

# Not a valid GTIN 13 barcode
#print(gtin13_calc(1234567890987))

# Required to report that the input isn't all digits
#print(gtin13_calc('A34567890987'))

# Required to report that the input should be 12 or 13 digits long
#print(gtin13_calc('A3456789098fffssd7'))

# Required to report that the input should be 12 or 13 digits long
#print(gtin13_calc('A345'))

print(validate_gtin13_barcode_check_digit('9400550619775'))
print(calculate_gtin13_barcode_check_digit('940055061977'))
