#Instructions:
#The code will ask for a year, assume that it's an integer, and tell you if it is a leap year or not.
#The code will not function with inputs that are not integers. To test the code, I ran it using the debugger on Visual Studio.


#take year from user
print("enter your year.")
input_year = input()


#converts input to integer, assumes the input is always an integer
input_year = int(input_year)


#Checks if the year is divisable by 4 with no remainder
if input_year % 4 == 0:

    #checks if the year is divisable by 4 and 100 with no remainder
    if input_year % 100 == 0:

        #if the year is divisible by 4, 100, and 400, the year is a leap year.
        if input_year % 400 == 0:
            print("Your inputted year: ", input_year, " is a leap year.")

        #if the year is divisible by 4 and 100 but not 400, it is not a leap year.
        else: 
            print("Your inputted year: ", input_year, " is not a leap year.")

    #if the year is divisible by 4 but not by 100, the year is a leap year.
    else:
        print("Your inputted year: ", input_year, " is a leap year.")

#if the year is not divisible by 4, we know that it is not a leap year.
else:
    print("Your inputted year: ", input_year, " is not a leap year.")