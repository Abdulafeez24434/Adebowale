# # name = input ("What is your name?")
# # age =int(input ("how old are are you?"))
# # current_year = 2019
# # if(current_year%4==0 and current_year%100!=0 or current_year%400==0):
# #     comment = f"hello{name} you are {age}, you were born in {2019-int(age)}. Your birth year is a leap year"
# # else:
# #     comment =  f"hello{name} you are {age}, you were born in {2019-int(age)}. Your birth year isn't leap year"
# # print (comment)

# word = input('please enter word : ')
# reversed_word = word[::-1]
# print(f"{word} is a palindrome : {word ==reversed_word}")
        # ASSIGNMENT 1
# names = [("Shade", "f"), ("Muyiwa","m"),("Tayo","m"), ("Kemi","f")]
# saluted_names = map(lambda x : " Mr " +x[0] if x [1] == "m" else " Mrs " +x[0], names)
# print(list(saluted_names))
        # ASSIGNMENT 2
# three_friends = ["Shola", "Ayo", "Tunde"]
# friends_no = (len(three_friends))
# candies = int(input("number of candies : "))
# g = int(candies/friends_no)
# remainder = int(candies % 3)
# statement = f'number of candy to be shared is : {g}\nnumber of candies to be crushed : {remainder}'
# print(statement)
        # ASSIGNMENT 3
# import random
# dice1 = random.randint (1,6)
# dice2 = random.randint (1,6)

# if (dice1 ==6) & (dice2 ==5) :
#     print("you won")
# else :
#     print("try again")