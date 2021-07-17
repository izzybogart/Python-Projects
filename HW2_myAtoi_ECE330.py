#The function returns an integer from a user inputted string, i.e. user inputs 123abc or 123.76 the function will only return the integer 123.
def myAtoi(s):
    #initialize the output to be zero
    output = 0
    #initialize sign to be +
    sign = 1
    #ignore whitespaces
    i = 0
    while(s[i] == ' '):
        i+=1
    #change sign if needed
    if(s[i] == '-'):
        sign = -1
        i+=1
    #fixed issued with not reading in the + sign
    if(s[i] == '+'):
        sign = 1
        i+=1
    #check for valid characters
    while(i< len(s) and s[i] >= '0' and s[i] <= '9'):
        #overflow check
        if(output> (2147483646//10) or
            output == (2147483646//10)):
            if(sign == 1):
                return 2147483646
            else:
                return -2147483647
        output = output * 10 + (ord(s[i])- ord('0'))
        #ord returns the Unicode equivalent of an argument of
        #a string
        i+= 1
    return output * sign

#Driver code
InputS = input("Enter in a number:")
InputStoN = myAtoi(InputS)
