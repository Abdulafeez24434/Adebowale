# # # x = 20
# # # y = 30
# # # mynumber = 20.234
# # # rounded_num = round(mynumber,2)
# # # print(rounded_num)
# # # num = 22
# # den = 7
# # pi = num/den
# # print(pi)
# # rounded_num = round(pi,3)
# # print(rounded_num)
# name = "Elson"
# surname = "john"
# fullname = name + " "+ surname
# print(fullname)

# day = "20"
# month = "may"
# year = "2019"
# print(day + "/" + month + "/" + year)

# pi = 22/7
# print (pi)
# statement = "pi is "+ str(round(pi,2))
# print(statement)

# akara = input("please how many akara you want : ")
# akanmu = input ("please how many akanmu you want : ")
# print (akara, akanmu)

# akara_statement = "you bought"  + akara + " " "akanmu"
# akanmu_statement = "you bought" + akanmu +" " "akara"
# print(akara_statement) 
# print(akanmu_statement)

# akara_price = 20
# akanmu_price = 50

# bill = "your bill is : $ " + str(akara_price * int(akara) + akanmu_price * int(akanmu))
# print(bill)

# name = input ("please enter your name : " )
# age = input ("please enter age : " )

# comment = f"hello {name} you are {age}, you were born in {2019 -int(age)}"
# print(comment)

# shirt_price = 200
# jeans_price = 250
# tshirt_price = 150
# nativeattire_price = 200

# clothes_washed = input('Please how many clothes did you wash?')

# shirt = input('how many shirt washed?')
# jeans = input('how many jean washed')
# tshirt = input('how many t shirt washed')
# native = input('how many native attire washed')

# # shirt_statement = "you washed" +  shirt +  " " + "shirt"
# # jeans_statement = "you washed" + jeans + " " + jeans
# # tshirt_statement = "you washed" + tshirt + " " + tshirt

# # print(clothes_washed)
# # print(shirt , jeans, tshirt , native )
# # print(shirt_statement)
# # print(jeans_statement)
# # print(tshirt_statement)

# # name = input("please your name? :")
# # print(name[1] ,name [3] ,name [5])
# # print(name[-1])
# # print(name[0:5])

# word = input("please type in a word: ")
# length_of_word = input("please input_length_of_word: ")

# half_length_of_word = int(int(length_of_word)/2) - 1
# two_chars_up = half_length_of_word + 2

# first_two = word[0:2]
# last_two = word [-2:]
# mid_point = word[half_length_of_word: two_chars_up ]

# # statement = f"{first_two}{mid_point}{last_two}"
# statement = first_two + mid_point + last_two

# print(statement)
# # print(word[half_length_of_word: two_chars_up ])

# word = "sweet mum"
# slice = word[:-4]
# print(slice)

# x = 20
# x += 1
# print(x)
# x +=1
# print(x)

# a = int(input("what is your a : "))
# b = int(input("what is your b : "))
# c = int(input("what is your c : "))
# f = (b**2 - (4*a*c)) ** 0.5 
# x1 = (-b + f)/(2*a)
# x2 = (-b - f)/(2*a)
# print(x1, x2)

# age = int(input("please enter your age : "))

# can_drink = age >= 20
# can_pay_tax = age >= 18
# can_take_pension = age > 60
# can_retire = age == 40

# statement = f"Can drink : {can_drink}\nCan pay tax : {can_pay_tax}\nCan take pension : {can_take_pension}\nCan now retire : {can_retire}"

# print(statement)

# word = input('please enter word : ')
# response = 'a'not in word or 'e' not in word or 'o'not in word or 'u'not in word
# print(f"{word} contains vowels :{response}")

# a = int(input("type a number : "))
# b = int(input("type a number : "))
# c = int(input("type a number : "))
# d = int(input("type a number : "))
# x = (a*d) + (c*b)
# y = b*d
# print(f"{x}/{y}")

# fraction = input("enter a fraction in the format 'a/b + c/d' : ")
# splitted_fraction = fraction.split("+")
# frac1 = splitted_fraction[0]
# frac2 = splitted_fraction[1]

# splitted_frac1 = frac1.split('/')
# splitted_frac2 = frac2.split('/')

# a = splitted_frac1[0]
# b = splitted_frac1[1]
# c = splitted_frac2[0]
# d = splitted_frac2[1]

# print(fraction)
# print(splitted_fraction)
# print(splitted_frac1)
# print(splitted_frac2)
# print(a,b,c,d)

# frac1, frac2 = fraction.split("+")

# a, b, c, d = *frac1.split('/'), *frac2.split('/')
# print(a,b,c,d)

# date_of_birth = input("please your dob in format yyyy-mm-dd  : ")
# year = date_of_birth.split("-")
# print(year[0])

# print(1,2,3,sep = "\n", end = "-")
# print(1,2,3,sep = "\n")
# print("new line")

# file = open("my_data.csv", '')
# print("name","age","state","due", file = file,sep =",")
# print("ade","20","osun_state","20000", file = file,sep =",")
# file = open("my_data.csv", 'w')
# details = input("insert your details in this format Name,Age,State,Due : ")
# splitted_details = details.split(",")
# print(splitted_details[0],splitted_details[1],splitted_details[2],splitted_details[3],file = file,sep =",")

# filename = "lyrics.txt"
# mode = "r" #read mode open
# data = open(filename, mode)
# lyrics = data.read()
# print(lyrics)

# filename = "file.csv"
# mode = "w" #read mode open
# file = open(filename, mode)
# text = "Atha, science, eating"
# file.write(text)

# my_range =range(20,60,2)
# print(my_range)
# print(type(my_range))
# print(list(my_range))
# print(list(reversed(my_range)))

# x = [1,2,5,3,10,1,0,4]
# print(sorted(x, reverse = True))

# x = list("Alamin")
# print(sorted(x))

# my_list = ["Seed", "Bee", "A", "Checked", "Print"]
# print(sorted(my_list, key =len, reverse = True))

# my_dict =dict(a=20, b=30)
# print(my_dict)
# print(my_dict['a'])

# x = set("Abimbola")
# print(sorted(x)

# nums = [1,2,3,4,5]
# mapped = map(lambda x : x*2, nums)
# print(list(mapped))

# names = ["Ade", "John", "Shola"]
# mapped = map(lambda x : " Mr " +x, names)
# print(list(mapped))

# word = "Sharp"
# word = [000]
# print(any(word))

# word = "ADEBOWALE".lower()
# print(word)
# word = "ademuyiwa".upper()
# print(word)

# word = input('please enter word : ').upper()
# response = 'a'in word or 'e'in word or 'o'in word or 'u'in word
# print(f"{word} contains vowels :{response}")

# word = input("please input a word that start with 'PRE' : ")
# replace_word = word.replace("pre", "post")
# print(replace_word)

# text = ["gem", "hem", "blem", "chem"]
# mapped = map(lambda x : x.replace("e","a"), text)
# print(list(mapped))

# my_data = [1,3,1,2,2,4]
# mapped = map(lambda x : x-2.1, my_data)
# print(list(mapped))

# my_data = [1,3,1,2,2,4]
# mean = sum(my_data)/len(my_data)
# mapped = list(map(lambda x : (x-mean)**2, my_data))
# print(mapped)
# sum_of_squares = sum(mapped)
# print(sum_of_squares/(len(my_data)-1))

# word = ["Hello", "World"]
# print(''.join(word))

# filename = "Bsg.txt"
# mode = "r" #read mode open
# data = open(filename, mode)
# lyrics = data.read()
# # print(lyrics)
# print(lyrics.find("Lupita"))
# print(lyrics.count("skin"))

# if 'foo' in ['foo', 'bar', 'baz']:       
#     print('Outer condition is true')      

#     if 10 > 20:                           
#             print('Inner condition 1')        

#     print('Between inner conditions')     

#     if 10 < 20:                          
#              print('Inner condition 2')       

#     print('End of outer condition')       
# print('After outer condition')

# behaviour = input("enter good or bad : ")
# age = int(input("enter your age : "))
# if behaviour == "good" and age > 18 :
#     print("you get a game")
# if behaviour =="good" and age < 18 :
#     print("you get a pc")
# if behaviour == "bad" :
#     print("you are left alone")

# if 'b' in 'bar':
#     print('foo')
# elif 1/0:
#     print("this won't happen")
# elif 'var':
#     print("this wont't either")

# score = int(input("enter your score : "))
# status = 'Yess !!! pass' if score > 50 else 'Aww! fail'
# print(status) 

# x = 3
# s = ('foo' if (x == 1) else ('bar' if (x == 2) else ('baz' if (x == 3) else ('qux'if (x == 4) else 'quux'))))
# print(s)

# question1 = input('Are you okay ? : ')
# if question1 == 'True' :
#     print('please get a life')
# else: 
#     question2 = input('do you have pain ? : ')
#     if question2 == 'False' :
#         print('unable to diagose now')
#     else:
#         question3 = input('did you sleep well " : ')
#         if question3 == 'False' :
#             print('try to sleep')
#         else:
#             question4 = input('have you done hardwork ? : ')
#             if question4 == 'True' :
#                 print('try to sleep')
#             else:
#                 question5 = input('do you have a fever ? : ')
#                 if question5 == 'False' :
#                     print('inconclusive please see a doctor')
#                 else:
#                     question6 = input('are you vomitting ? : ')
#                     if question6 == 'False' : 
#                         print('take some anti-malaria')
#                     else:
#                         print('please see a doctor')

# a = ['foo', 'bar', 'baz']
# for i in a :
#     print(i)

# mean = sum(range(20)) / len(range(20))
# for i in range(20):
#     print(i, i-mean)

# print("x".center(4), "|","x_bar".center(7), "|", "(x_bar)**2".center(11),  sep = "")
# print("___".center(4), "|","____".center(7), "|","_______".center(11), sep = "")
# n = 5
# mean = sum(range(n)) / len(range(n))
# for i in range(n):
#     print(f"{i}".center(4), "|",f"{i-mean}".center(7), "|",f"{(i-mean)**2}".center(11), sep = "")

# names = ["John","Clam"]
# for i in names:
#     print("Hello,",i)

# words = input('type a words : ')
# vowel_sounds = ['a','e','i','o','u']
# total_vowels = 0
# for i in words:
#     if i in vowel_sounds:
#         print(i)
#         total_vowels = total_vowels + 1
# print(f"Total vowels : {total_vowels}")

# words = input('type a words : ')
# vowel_sounds = ['a','e','i','o','u']
# total_vowels = 0
# for vowel_sounds in vowel_sounds:
#     if vowel_sounds in words:
#         print(vowel_sounds)
#         count = words.count(vowel_sounds)
#         total_vowels = total_vowels + count
# print(f"Total vowels : {total_vowels}")

# words = input('type a words : ')
# vowel_sounds = ['a','e','i','o','u']
# total_vowels = 0
# print(f"vowel | Count")
# print(f"______|______")
# for vowel_sounds in vowel_sounds:
#     if vowel_sounds in words:
#         count = words.count(vowel_sounds)
#         total_vowels = total_vowels + count
#         print(f"{vowel_sounds.center(6)}|{str (count).center(6)}")
# print(f"Total vowels : {total_vowels}")

# for i in range(10):
#     print(i)
#     if i ==5:
#          break

# word = input("Enter word : ")
# for i in word:
#     print(i)
#     if i =='?':
#         break

# filename = "twist.txt"
# raw_data = open(filename, "r")
# data = raw_data.readlines()
# for line in data:
#     print(line)
#     print()
#     if "canoed" in line:
#         break

# scores = [20, 30, 70, 10, 67, 50]
# import random
# for score in scores:

#     c_assess = random.randint(10,30)
#     f_score = score + c_assess

#     marked_up = int(f_score * 1.2)
#     if f_score > 70:
#         print(score, c_assess, f_score, f_score)
#         continue

#     print(scores, c_assess, f_score, marked_up, "marked_up")

# loan_amount = 300000
# rate = 0.05
# time = 2
# payments_per_year = 12
# principal = loan_amount

# repayment = (principal*(rate/payments_per_year))/(1-(1+(rate/payments_per_year))**((payments_per_year*-1)*time))

# no_payments = time * payments_per_year

# print("Period".center(5),"AMOUNT".center(11),"INTEREST".center(11),"PRINCIPAL".center(11), "BALANCE".center(11),"\n ")

# loan_interest = 0
# for payment in range(no_payments + 1):


#     if payment == 0:
#         print(str(payment).center(5),"-".center(11), "-".center(11), "-".center(11), str(loan_amount).center(11))
#     else:
#         interest = loan_amount * (rate/payments_per_year)
#         loan_amount = loan_amount - (repayment - interest)
#         principal = (repayment - interest)
#         principal = round(principal,2)
#         loan_interest += interest
#         repayment, interest, loan_amount = round(repayment,2), round(interest,2), round(loan_amount,2)

#         print(str(payment).center(5),str(repayment).center(11), str(interest).center(11), str(principal).center(11), str(loan_amount).center(11))
# print(loan_interest)

# import random
# choices = ["G", "G", "C"]
# wins = 0
# loses = 0
# for i in range(100):
#     choice = random.choice(choices)
#     if choice == "":
#         print("Yesss!!! You won..!!!")
#         wins+=1
#     else :
#         print("ooops You lost..!!!")
#         loses+=1
# print("wins: ", wins, "Loses: ", loses)

# import random

# ## HOLDER ###
# choices = ["G", "G", "C"]
# random.shuffle(choices)


# trials = 0
# wins = 0
# while trials < 1000:
#   trials += 1
#   guest_choice = random.choice(choices)

#   if guest_choice == "C":
#     # print("Win!!")
#     wins += 1
#   elif guest_choice == "G":
#     # print("Loose!!")
#     pass

# prob_success = wins/trials
# print(f"Holder : {prob_success * 100}%")


# trials = 0
# wins = 0

# while trials < 1000:
#   trials += 1
#   guest_choice = random.choice(choices)

#   temp_choices = choices.copy()
#   temp_choices.remove(guest_choice)
#   temp_choices.remove("G")

#   guest_choice = temp_choices[0]

#   if guest_choice == "C":
#     # print("Win!!")
#     wins += 1
#   elif guest_choice == "G":
#     # print("Loose!!")
#     pass

# prob_success = wins/trials
# print(f"Switcher : {prob_success * 100}%")

# n = 5
# while n > 0:
#     n -=1
#     print(n)

# n = 5
# for i in range(n):
#     n = n-1
#     print(n)

# x = "boy toys junk"
# y = "mum girl luch"
# n = 0
# word_length = len(x)
# while n < word_length:
#     print(x[n], y[n])
#     n+=1

