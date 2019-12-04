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

                # BUILDING A DICE GAME
# import random
# a,b = random.randint(1,6), random.randint(1,6)
# c,d = random.randint(1,6), random.randint(1,6)
# e,f = random.randint(1,6), random.randint(1,6)
# print("play this game with just 3 tries only ")
# input("press enter to roll : ")
# if a ==6 and b ==6:
#         print(a,b)
#         print("yesss you won!!!")
# else:
#         print(a,b)
#         print("you have two tries left")
#         input("press enter to roll : ")
#         if c ==6 and d ==6:
#                 print(c,d)
#                 print("yess you won!!!")
#         else:
#                 print(c,d)
#                 print("you have one left tries")
#                 input("press enter to roll : ")
#                 if c ==6 and d ==6:
#                         print(e,f)
#                         print("yesss you won")
#                 else:
#                         print(e,f)
#                         print("game over!!!")


                # BUILDING A DICE GAME
# import random
# for i in range(5):
#         dice1 = random.randint(1,6)
#         dice2 = random.randint(1,6)
#         print("dice1", dice1, "dice2", dice2)
#         if dice1 ==dice2 and dice1 ==6:
#                 print("Yeah!!! you won")
                
#                 break
#         else:
#                 print("ooops! lost")
#         input("press enter to try again")


                # BUILDING A MULTIPLICATION TABLE
# for i in range(1,5):
#         for n in range(1,5):
#                 print(f"{n}*{i} = {n*i}".center(12), end = "\t")
#         print("\n")


                # BUILDING A TIMER
# import time
# boom = int(input("count"))
# while boom > 0:
#         time.sleep(1)
#         print(boom, "\r", end ="")
#         boom -=1
# print("BLAST OFF!")

                # BUILDING A TIMER WITH SOUND
# import time
# import winsound

# sound = winsound.Beep
# for i in reversed(range(20)):
#         time.sleep(1)
#         print(i, "\r", end ="")
#         sound(500,1000)
# else:
#         sound(1000,8000)
