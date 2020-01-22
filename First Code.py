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

# mylist = [1,2,3,4,5,6]
# print(mylist)

# name = "shalewa"
# my_second_list = list(name)
# print(my_second_list)

# products = "shoes,bags,rings,shirts"
# my_third_list = (products).split(",")
# print(my_third_list)

# # my_third_list.append("shorts")
# attempts = 5
# while True:
#     already_counted = []
#     for item in my_third_list:
#         if item not in already_counted:
#             occurences = my_third_list.count(item)
#             already_counted.append(item)
#             print(item, occurences)

#     action = input("What would you like to do : ")

#     if action == "add":
#         for item in my_third_list:
#             occurences = my_third_list.count(item)
#             print(item, occurences)
            
#         new_prop = input("Enter a new prop : ")
#         my_third_list.append(new_prop)
#         print(my_third_list)

#     elif action == "rem":
#         new_prop = input("Enter a prop to remove : ")
#         my_third_list.remove(new_prop)
#         print(my_third_list)
    
#     attempts -= 1
#     if attempts == 0:
#         print("You have run out of attempts...!!")
#         break

# import random
# random_nums = []
# for i in range(20):
#     round_num = random.randint(1,5)
#     random_nums.append(round_num)
# print(random_nums)
    
# already_counted = []
# for item in random_nums:
#     if item not in already_counted:
#         occurences = random_nums.count(item)
#         already_counted.append(item)
#         print(item, occurences)    

# word = "shayo"
# cap_word = [x.upper() for x in word]
# print(cap_word)

# q = [1,2,3,4,5,6,7]
# squared = [x**2 for x in q]
# print(squared)

# my_bio = {"Name": 'afeez', "Age": "21", "Sex":'Male'}

# print(my_bio['Name'].upper(), "is", my_bio["Age"], "and", "is", my_bio["Sex"].lower())

# my_bio["hobby"] = "Music"
# print(my_bio.keys())
# print(my_bio)

# print(my_bio["hobby"])
# my_hobby = my_bio.get("hobby")
# print(my_hobby)

# my_strenght = my_bio.get("names", "keys does not exit.!!")
# print(my_strenght)
# my_bio['age'] = 30
# print(my_bio)
# del my_bio["age"]
# print(my_bio)

# new_num = dict(
#             (
#                 (1, [2,3,"name"]),
#                 (2, 3),
#                 (4,1)
#             )
#             )
# print(new_num)

# risky = "risky_lyrics"
# bsg = "bsg_lyrics"

# file = open(f"{risky}.txt", "r")

# data = file.readlines()
# lyrics_dict = {}
# line_num = 1
# lyrics_dict[risky] = {}

# for line in data:
#     # print(line)
#     lyrics_dict[line_num] = line
#     line_num+=1
# file.close()

# file = open(f"{bsg}.txt", "r")

# data = file.readlines()
# line_num = 1
# lyrics_dict[bsg] = {}

# for line in data:
#     # print(line)
#     lyrics_dict[bsg][line_num] = line
#     line_num+=1
# file.close()

# print(lyrics_dict.Keys())

# while True:
#     requested_song = int(input("please what line would you like to get: "))
#     print(lyrics_dict.keys())
#     requested_line = int(input("please what line would you like to get: "))
#     print(lyrics_dict[requested_song][requested_line])

# import requests
# import matplotlib.pyplot as plt

# url = "http://checklight.pythonanywhere.com/streets"
# response = requests.get(url)
# data = response.json()
# print(data.keys())

# print(type(data["streets"]))

# streets = data["streets"]
# for street in streets:
# #     print(type(street))
# #     print(street.keys())
# #     print(street.get("name").center(20), "-", street.get("last_no_light").center(20), "-", street.get("lga"))
# #     print("\n\t ----------TIMELINES----------\n")
#     timelines = street.get("history").get("time_line")
# #     for timeline in timelines:
# #         status = "Up Nepa" if timeline.get("status") == 1 else "Down Nepa"
# #         period = round(timeline.get("period")/3600,1)
# #         time = timeline.get("time")
# #         print("\t", str(time).center(12), (str(period)+"hours").center(12), str(status).center(12), sep = " | ")

# daily_supply = street.get("history").get("daily_supply")
# print(daily_supply)

# labels = daily_supply["labels"]
# values = daily_supply["values"]

# plt.bar(labels, values)
# plt.title(street.get("name"))
# plt.show()

# import requests
# url = "http://checklight.pythonanywhere.com/get_readings/1x0d001/5/"
# response = requests.get(url)
# data = response.json()
# print(data.keys())
# streets = data["streets"]
# count = []
# for street in streets:
#     # print("\n", street.get("time").center(12), " | ", street.get("status"))
#     if (street.get("status")) == 0:
#         print("\n", street.get("time").center(12), " | ", street.get("status"))
#         count.append(street.get("status"))
# print(count)
# print(len(count))

# import requests
# url = "http://checklight.pythonanywhere.com/get_readings/1x0d001/5/"
# response = requests.get(url)
# data = response.json()
# streets = data["streets"]
# days = {}

# for street in streets:
#     status = street["status"]
#     time = street["time"]
#     day = time[5:7]

#     if status == 0:
#         if day not in days:
#             days[day] = 0
#         days[day] += 1
#         print(day, status)
    
# print(days)

# import requests
# devices = ["1x0d001", "1x0d002", "1x0d003", "1x0d004"]
# all_devices ={}

# for device in devices:
#     url = f"http://checklight.pythonanywhere.com/get_readings/{device}/12/"

#     response = requests.get(url)
#     data = response.json()

#     streets = data["streets"]
#     days = {}

#     for street in streets:
#         status = street["status"]
#         time = street["time"]
#         day = time[5:7]

#         if status == 0:
#             if day not in days:
#                 days[day] = 0
#             days[day] += 1
#             # print(day, status)
#     all_devices[device] = days
# print(all_devices)

# import citylist
# import requests
# data = citylist.citylist


# user_city = input("Please enter city name : ")
# user_country = input("Please enter country name : ")

# def fetch_id(user_city, user_country, data):
#     city_id = ""

#     for city in data:
#         if city["name"] == user_city and city["country"] == user_country:
#             city_id = city["id"]
#             print(city["name"], city["country"], city["id"], "\n\n\n\n\n")
    
#     return city_id

# id = fetch_id(user_city, user_country, data)
# print(id)
# api_key = "336b102582e7d317c464efd5e6ac86aa"
# url = f"http://api.openweathermap.org/data/2.5/forecast?id={id}&APPID={api_key}"

# r = requests.get(url)
# # print(r.json())
# file_name = "weather_data.py"

# file = open(file_name, "w")
# print(r.json(), file= file)
# print(r.json())


#                       #####  OBJECT ORIENTED PROGRAMME  #####

# class Animal:
    
#     status = "Animate" # CLASS ATTRIBUTE

#     def __init__(self, limbs, covering, food_type, name, habitat, family ):
#         self.limbs = limbs
#         self.covering = covering
#         self.food_type = food_type
#         self.habitat = habitat
#         self.family = family
#         self.__name = name ##__NAME IS AN ENCAPSULATED ATTRIBUTE

#     def set_Name(self, new_name): #SETTER FOR NAME BECAUSE NAME IS ENCAPSULATED
#         self._name = new_name

#     def get_Name(self):
#         return self.__name





# billy = Animal(name = "Billy", limbs = 4, covering = "fur", habitat = "Terrestrial", food_type = "Omnivore", family = "Dog")

# rhodes = Animal(name = "Rhodes", limbs = 4, covering = "Feathers", habitat = "Aboreal", food_type = "Omnivore", family = "Bird")



# print(type(billy))
# print(billy.status)
# print(billy.food_type)
# print(billy.covering)


#  class account:
    #     #  class attribute
#     type = 'parent'
#     def __init__(self, acct_no_param, name_param):
#         # insatnce attribute
#         self.acct_no = acct_no_param
#         self.name = name_param
#         self.bal = 0

#     def deposit(self, amount):
#         self.bal +=(amount)
#         print(f"successfully added {amount} to {self.name} balance, \nNew balnce = {self.bal}\n")
#     def withdrawal(self, amount):
#         self.bal -=amount
#         print(f'successfully withdraws {amount} from {self.name} balance, \n New balance = {self.bal}\n')


# my_acct = account(acct_no_param ="301229409", name_param = "Bruno")
# my_acct2 =account(acct_no_param = "301224300", name_param = "salami")
    
    
# print(my_acct.name)
# print(my_acct.acct_no)
# print(my_acct.type)
# (my_acct.deposit(5000))
# (my_acct.withdrawal(1000))

# print(my_acct2.name)
# print(my_acct2.acct_no)
# print(my_acct2.type)
# (my_acct2.deposit(12000))
# (my_acct2.withdrawal(1000))

# class current_acct (account):
#     type ="current"

#     def __init__(self, acct_no_param, name_param, dollar_bal = 0 ):
#         account.__init__(self, acct_no_param, name_param)
#         self.dollar_bal = dollar_bal

# class savings_acct(account):
#     type = "savings"
#     def __init__(self, acct_no_param, name_param, interests = 0.5 ):
#         account.__init__(self, acct_no_param, name_param)
#         self.interests = interests

# # my_curr_acct = current_acct(acct_no_param = "30129409", name_param = 'john')
# my_savings_acct = savings_acct(acct_no_param = "301229409", name_param = "sule")
# # print(my_curr_acct.name)
# # print(my_curr_acct.type)
# # print(my_curr_acct.dollar_bal)

# print(my_savings_acct.name)
# print(my_savings_acct.type)
# print(my_savings_acct.interests)


# filename = "application_data.csv"
# mode = "r"
# file = open(filename, mode)
# data = file.readlines()
# names_of_columns = data[0].replace(" ", " ")

# class Application: 
#     def __init__(self, name_of_columns,  number_of_columns, number_of_rows, name_of_numeric_columns, name_of_text_columns):
#         self.name_of_columns = name_of_columns
#         print(names_of_columns)

# l = ('a,b,c')
# n= (1,2,3)

# ln = zip(l,n)
# print(ln)

# import datetime, random, json

# def generate_acct_no():
#     no = [str(random.randint(0,9)) for i in range(10)]
#     acct_no = "".join(no)

#     return acct_no
        
# class Customer:

#     def __init__(self, name = "none", username = str(datetime.datetime.now()), password = "11111111"):
#         self.name = name
#         self.username = username
#         self.password = password
#         self.creation_date = str(datetime.datetime.now())

#     def details(self):
#         print(self.name)
#         print(self.username)
#         print(self.creation_date)
#         return "this is my empty return"


# class Account:

#     def __init__(self, type, customer, account_no = generate_acct_no()):
#         self.customer = customer
#         self.__balance = 0
#         self.creation_date = str(datetime.datetime.now())
#         self.type = type
#         self.account_no = account_no 

#     def get_balance(self):
#         print(self.__balance)
    
#     def details(self):
#         print(self.customer.name)
#         print(self.customer.username)
#         print(self.customer.creation_date)
#         print(self.account_no)

#     def save(self):
#         Storage.store(type = self.type, account_no = self.account_no, acct_creation_date = self.creation_date, name = self.customer.name, username = self.customer.username, password = self.customer.password, cust_creation_date = self.customer.creation_date )



# class Storage():

#     @staticmethod
#     def store(**kwargs):
        
#         data = json.dumps(kwargs)
#         file = open("acct_db", "w")
#         file.write(data)

# cust_1 = Customer("afeez", "boss_of_game", "qwerty")
# acct1 = Account("savings", cust_1)

# acct1.details()
# acct1.save()

# class Table:
    
#     def __init__(self, filename):

#         self.filename  = filename

#         col_data = self.get_col_names()
#         row_data = self.get_num_rows()

#         self.col_names = col_data[1]
#         self.col_count = col_data[0]
#         self.row_count = row_data


#     def get_col_names(self):

#         col_row = open(self.filename, "r").readlines()[0]
#         col_names = col_row.split(",")

#         print("COLUMNS IN FILE : ")
#         for name in (col_names):
#             print(f"\t{name}")

#         num_of_cols = len(col_names)
        
#         return num_of_cols, col_names

#     def get_num_rows(self):

#         num_rows = len(open(self.filename, "r").readlines())-1

#         return num_rows

#     def get_numeric_cols(self):

#         lines = open(self.filename, "r").readlines()
#         lines.pop(0)

#         list_of_tuples = map(lambda string: string.split(","), lines)

#         unzipped_data = zip(*list_of_tuples)

#         text_col = []
#         num_col = []
#         count = 0

#         for line in unzipped_data:
            
#             if not any(map(lambda x: x.replace(".", "").isnumeric(), line)):
#                 num_col.append(self.col_names[count])
#             else:
#                 text_col.append(self.col_names[count])


#             count += 1

#         print(text_col)
#         print(num_col)
            

# new_data = Table("DNMM_CDD_18C.csv")
# print(new_data.filename)
# new_data.col_names
# print(new_data.row_count)
# new_data.get_numeric_cols()

# # file = open("DNMM_CDD_18C.csv", "r")
# # print(len(file.readlines())-1)


#                       ####    SQL    #####
#                 ####### CREATE PRODUCT TABLE  ######

# import pymysql.cursors

# connection = pymysql.connect(host = 'localhost',
#                             user = 'root',
#                             password = '',
#                             db = 'my_db',
#                             charset = 'utf8mb4',
#                             cursorclass=pymysql.cursors.DictCursor)

# with connection.cursor() as cursor:
#     #create a new record

#     sql_cmd = f'create table product (id int(3) AUTO_INCREMENT PRIMARY KEY NOT NULL, name varchar(30), price int(5), weight float(5,5))'

#     cursor.execute(sql_cmd)
#     connection.commit()

#               ###### INSERT SINGLE USER  ########
# import pymysql.cursors

# connection = pymysql.connect(host = 'localhost',
#                             user = 'root',
#                             password = '',
#                             db = 'my_db',
#                             charset = 'utf8mb4',
#                             cursorclass=pymysql.cursors.DictCursor)

# with connection.cursor() as cursor:
#     #create a new record
#     sql_cmd = 'INSERT into student (f_name, l_name, age, address,email, salary) values ("lateef", "desginwork", 26, "bariga, lagos", "all4lateef@gmail.com", 600000)'

#     cursor.execute(sql_cmd)
#     connection.commit()
# print(sql_cmd)

#                   ###### INSERT RANDOM USER  ########
# import pymysql.cursors

# connection = pymysql.connect(host = 'localhost',
#                             user = 'root',
#                             password = '',
#                             db = 'my_db',
#                             charset = 'utf8mb4',
#                             cursorclass=pymysql.cursors.DictCursor)


# with connection.cursor() as cursor:
#     import random 

#     names = open('randomnames.txt', 'r').read()
#     emails = ['@gmail.com', '@yahoo.com', '@live.com']
#     splitted_names = names.splitlines()
#     for name in splitted_names:
#         fname, lname = name.split()
#         random_email = random.choice(emails)
#         email = f"{fname[:3]}{lname[:3]}{random_email}"
#         age = random.randint(10, 50)
#         salary = random.randint(100000, 500000)
#         print(f"firstname -  {fname},  lastname -  {lname},  Age -  {age},  email-  {email},  salary - {salary}")
#         sql_cmd = f'INSERT into person (f_name, l_name, age, address,email, salary) values ("{fname}", "{lname}", {age} ,"abuja",  "{email}", "{salary}")'
        
#         cursor.execute(sql_cmd)
#         connection.commit()
# print(splitted_names)
# 

#                       ###### CREATE ORDER TABLE   #######
import pymysql.cursors

connection = pymysql.connect(host = 'localhost',
                            user = 'root',
                            password = '',
                            db = 'my_db',
                            charset = 'utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
# with connection.cursor() as cursor:
    #create a new record
    # sql_cmd =  f'create table orders (person_id int, FOREIGN KEY(person_id) REFERENCES person(person_id), product_id int, FOREIGN KEY(product_id) REFERENCES product(id), order_date Date, qty int(5))'

    # cursor.execute(sql_cmd)
    # connection.commit()

products = ["apple", "orange", "shoes", "knife", "cream"]
prices = [10, 4, 50, 10, 20]
weights = [5, 6, 7, 8, 8]

with connection.cursor() as cursor:
    for items in zip(products, prices, weights):
        pname = items[0]
        pprice = items[1]
        pweights = items[2]

        sql_cmd = f'INSERT INTO product (name, price, weight) values ("{pname}", "{pprice}", "{pweights}")'

        cursor.execute(sql_cmd) 
        connection.commit()
