#64 bit interger range is -9223372036775808 to 9223372036775807
print("Please enter in an integer")
x = int(input())
negative=""

if(x>0):
    intrev= str(x)[::-1] #intrev is a string of the numbers in x just reversed
    out = int(intrev)     #converts intrev to an int
else:                     #condition for negative numbers
    intrev = "-"+str(x)[::-1]
    for i in range(len(intrev)-1):
        negative = negative +intrev[i]
    out = int(negative)
#check for range
if(out>=-9223372036775808 or out<=9223372036775807):
    print("Your integer reversed is:")
    print(out)
else:
    print("NaN")
