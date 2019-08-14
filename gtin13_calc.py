def gtin13_calc(x):
    
    
    #print (len(x))
    #print(type(int(x)))

    #Determine if this is a whole check number


    try:

        #( len(x) == 13) and (type(int(x)) == int) # could I make this check neater?
        # Why did my code get past the line above when len(x)=12, bad. But not when it couldn't be converted to an integer eg the number included a letter?'
        
        # convert input to a list.
        x=[int(d) for d in str(x)]

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
        
    except:
        return 'Please enter a the ISBN-13 number, with or without the check number'
    
    #See if the check number was entered in by the user.  If so, tell them if the number is valid.
    if len(x)  == 13:
        check_no_entered = int(x[12])    
        if  check_no_entered == check_no_calc:
            return 'This is a valid gtin13 barcode.'
        else:
            return 'This is NOT a valid gtin13 barcode.'
    else:
        return check_no_calc



#Required to give 5
print(gtin13_calc('940055061977'))
#Required to give 2, it already has it's check digit.
print(gtin13_calc('9781861972712'))

print(gtin13_calc(1234567890987))
print(gtin13_calc('A34567890987'))