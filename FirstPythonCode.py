
#Runs through a range of 0 to 20, checks if the numbers are divisible by three and if so prints them,
#also prints "Bingo!" after every number that is also divisible by 5, and finally prints "---" for 
#numbers that are not divisible by 3.for i in range(20):
    if i%3==0:
        print(i)
        if i%5 == 0:
            print("Bingo!")
    print("---")
