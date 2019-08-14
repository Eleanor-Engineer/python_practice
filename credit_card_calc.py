def credit_card_calc(x,y):
    #print(len(x))
    #print(type(x))

    try:
        y == 'y' or y == 'n'
        check_dig_inc = y
        
        # convert the card number to a string or numbers.
        x=[int(d) for d in str(x)]

        # Remove the check number, if one was entered.
        if check_dig_inc == 'y':
            #extract the last digit entered
            check_no_entered = (x[len(x)-1]) 
            #remove the check digit from the card number
            x = x[:len(x)-1]
        else:
            check_no_entered = 'Check number not entered.'
       # Define variables for while loop
        sum = 0
        a=0
        # Do the loop for all the didgets, excluding the check digit.       
            # This method of checks is taken from https://en.wikipedia.org/wiki/Luhn_algorithm
        while a  < (len(x) ) :
            adding= (   (a+len(x)) % 2  + 1 ) * x[a]
            if adding > 9:
                adding = adding -9 
            sum += adding
            a = a + 1

        check_no_calc = -sum % 10
        
        #for error checking
        print('card number ',x,'check number entered:',)
        print(check_no_calc)


    except:
        return 'Please use the funciton like this: credit_card_calc( [credit card number, with or without the check number], [y/n to indicate if it includes the check number]'
    
    #See if the check number was entered in by the user.  If so, tell them if the number is valid.
    if check_dig_inc == 'y':
   
        if  check_no_entered == check_no_calc:
            return 'This credit card nubmber follows the maths rules, but to find out if it\'s valid please try it out by buying Hayley a coffee ;)'
        else:
            return 'This is NOT a valid credit card number.'
    else:
        return 'The check number is ', check_no_calc

#Full valid credit card number
print(credit_card_calc('5499740000000057','y'))

#Full valid credit card number
print(credit_card_calc(371449635398431,'y'))
#Full valid credit card number
print(credit_card_calc('36438999960016','y'))

#this should error
print(credit_card_calc('36d438999960016','y'))