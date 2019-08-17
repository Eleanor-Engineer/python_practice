def check_card_input(card_no,check_no_entered):
    if (check_no_entered is not 'y') and (check_no_entered is not 'n'):
        return 'Please use the funciton like this: credit_card_calc( [credit card number, with or without the check number], [y/n to indicate if it includes the check number]'
    elif len(str(card_no)) < 6 or len(str(card_no)) > 20:
        return 'Please enter a credit card number, with or without the check number.'
    elif str.isdigit(str(card_no)):
        return 'OK'
    else:
        return'Oops, looks like you entered some characters which aren\'t digits.'
        


def credit_card_calc(card_no,check_no_entered):
    #print(len(x))
    #print(type(x))
    #check if the user inputed the right functions
    if check_card_input(card_no,check_no_entered) is not 'OK':
        return check_card_input(card_no,check_no_entered)
    
    # convert the card number to a string or numbers.
    card_no=[int(d) for d in str(card_no)]

    # Pull out the check number the user entered, if applicable.
    if check_no_entered == 'y':
        #extract the last digit entered
        check_no_entered = (card_no[len(card_no)-1]) 
        #remove the check digit from the card number
        card_no = card_no[:len(card_no)-1]

    # Define variables for while loop
    sum = 0
    a=0
    # Do the loop for all the didgets, excluding the check digit.       
        # This method of checks is taken from https://en.wikipedia.org/wiki/Luhn_algorithm
    while a  < (len(card_no) ) :
        adding= (   (a+len(card_no)) % 2  + 1 ) * card_no[a]
        if adding > 9:
            adding = adding -9 
        sum += adding
        a = a + 1

    check_no_calc = -sum % 10
    
    if check_no_entered == 'n':
        return 'The check number is '+ str(check_no_calc)

    if  check_no_entered == check_no_calc:
        return 'This is a valid credit card number.'

        #Here is a more fun, and arguably more correct, way of indicating the number is valid
        #return 'This credit card number follows the maths rules, but to find out if it\'s valid please try it out by buying Hayley a coffee ;)'
    else:
        return 'This is NOT a valid credit card number.'


# create functions with similar names to Hayley's gtin13 barcode
def validate_credit_card_check_digit(x):
    return credit_card_calc(x,'y')
def calculate_credit_card_check_digit(x):
    return credit_card_calc(x,'n')


# Other checks with the old funciton names
##Full valid credit card number
#print(credit_card_calc('5499740000000057','y'))

##Full valid credit card number
#print(credit_card_calc(371449635398431,'y'))

##Full valid credit card number which should have 1 as the check number
#print(credit_card_calc(37144963539843,'n'))

##Full valid credit card number, but with a bad user input
#print(credit_card_calc('36438999960016','blank'))

##this should error
#print(credit_card_calc('36d438999960016','y'))


#Checks with Hayley style functin names.
#credit card number without check number which should have 1 as the check number.
print(calculate_credit_card_check_digit('37144963539843'))

##Full valid credit card number
print(validate_credit_card_check_digit('371449635398431'))

##Invalid credit card number
print(validate_credit_card_check_digit('371449635398436'))
