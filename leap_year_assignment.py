name = input ("What is your name?")
age =int(input ("how old are are you?"))
current_year = 2019
if(current_year%4==0 and current_year%100!=0 or current_year%400==0):
    comment = f"hello{name} you are {age}, you were born in {2019-int(age)}. Your birth year is a leap year"
else:
    comment =  f"hello{name} you are {age}, you were born in {2019-int(age)}. Your birth year isn't leap year"
print (comment)