# mynumber =20.234
# rounded_num = round(mynumber, 2)
# print(rounded_num)

# a=8
# b =2
# pi = a/b
# print(pi)
# round_pi = round(pi,2)
# print(round_pi)

# name = "Elson"
# surname = "john"
# fullname = name + " "+ surname
# print(fullname)

# day = "20"
# month = "may"
# year = "2019"
# print(day + "/" + month + "/" + year)

# pi = 6/3
# print (pi)
# statement = "pi is  " + str(round(pi,1)) 
# print (statement) 

# akara_price = 20
# akamu_price = 50
# akara = input('please how many akara do you want? :') 
# akamu = input ('how many scoops of  akamu do you want ? :')
# print (akara, akamu)

# akara_statement = "you bought"  + akara + " " + "akara" 
# akamu_statement = "you bought" + akamu + " "+  "akamu"
# print(akara_statement)
# print(akamu_statement)
# bill = "your bill is :" + str(akara_price * int(akara) + akamu_price * int(akamu) )
# print(bill)  

# name = input("Please your name?")
# age = input("please your age?")
 
# comment= f"hello {name} you are {age} years old. You were born in {2019 - int(age)}"
# print(comment)

# name = input("Please your name? ")
# print(name[1], name[3], name[5])
# print(name[-1])
# print(name[0:5])

# word = input("type in a word :")
# length_of_word = input("please input number of characters :")

# split = int(int(length_of_word)/2) - 1
# two_chars_up = split + 2
# first_two = word[0:2]
# last_two = word[-2:]
# mid_point = word [split : two_chars_up]
# statement = f"{first_two}{mid_point}{last_two}"
# print(statement)
# print(word[split:two_chars_up])

# word = "sweet mum"
# slice = word[:-5]
# print(slice)

# a = int(input("what is your a?"))
# b = int(input("what is your b?"))
# c = int(input("what is your c?"))
# num = ( (int(b)**2 ) - (4 * int(a*c) )  )** 0.5
# den = (2 * a)
# x1 = ((-b+num)/den)
# x2 = ((-b-num)/den)
# y = ((a**2)+(b**2))**0.5

# print(x1, x2)

# age = int(input('please enter your age :')) 

# can_drink = age >= 20
# can_pay_tax = age >= 18
# can_take_pension = age > 60
# can_retire = age == 40 

# statement = f"can drink : {can_drink}\n can pay tax : {can_pay_tax}\nCan take pension : {can_take_pension}\nCan now retire : {can_retire} "
# print(statement)

# file = open("my data.csv", 'w')
# # print(1,2,3,4, file = file, sep = ",")
# file= open("my_data.csv," 'a')
# print("name", "Age","state","Due", file= file,sep = ",")
# print("ade", 20, "osunstate", 20000, file= file,sep = ",")
# file = open('my_data.csv', 'w')
# details = input ('enter your details in this format name,age,state, dues:')
# splitted_details = details.split (",")
# print (splitted_details[0], splitted_details[1], splitted_details[3], file = file,sep = ",")


                        #  COMMON STRING OPRATIONS
# my_range = range(20, 60, 2)
# print(my_range)
# print(type(my_range))
# print(list(my_range))
# print(list(reversed(my_range)))

# x = [1,2,5,3,10,1,0,4]
# print(sorted(x, reverse = True))

# x= set("abimbola")
# print(set(x))

# my_list = ["seed", "bee", "a", 'cheeked', 'print']
# print(sorted(my_list, key = len, reverse= True))

# my_dict = dict(a=20, b=30)
# print(my_dict)
# print(my_dict['a'])

# nums = [1,2,3,4,5]
# mapped = map (lambda x : x*2, nums)
# print(list(mapped))

# names = ['ade', 'john', 'shola',]
# mapped = map(lambda x : " mr " + x, names)
# print(list(mapped))

# word = input ("please input a word") .lower()

# response = 'a' in word or 'e' in word or 'i' in word or 'u' in word
# print(f' contains vowels : {response}')


# word = input("please input a word thats start with 'PRE' : ")
# replace_word = word.replace("pre", "post")
# print(replace_word)

# text = ['gem', 'hem', 'blem', 'chem']
# mapped = map(lambda x : x.replace('e', "a"), text)
# print(list(mapped))

# data = [ 1, 3, 1, 2, 2, 4]
# mean = sum(data)/len(data)
# mapped = list(map(lambda a : (a-mean)**2, data))
# print((mapped))
# sum_of_squares = sum(mapped)
# n_1 = (len (data))
# print(n_1)
# print(sum_of_squares/(len(data)-1))

# a = ['hello', 'world']
# name = ' '.join(a)
# print(name)

# 
                 #    ASSIGNMENT 1
# import random 
# for x in range(2):
#    print(random.randint(1,6))
# if random.randint is (6,6) is True:
#     print("you win")
# else:
#     print("try again")

#                 #   ASSIGNMENT 2
# three_friends = ["bola", "chisom", "james"]
# no_of_friends = (len(three_friends))
# candies = int(input("number of candies:"))
# a =int(candies/no_of_friends)
# remainder = int(candies % 3)
# statement = f' number of candy to be shared is : {a}\n number of candies to be crushed : {remainder}'
# print(statement)

#             # assignment 3
# name = [(' ' 'Ade', 'm'), ([' ''shade', 'f']), ([' ' 'john', 'm']), ([' ' 'bolu', 'f'])]
# raw_saluted_name = map(lambda x : "Mr" +  x[0] if x[1] == "m" else "Mrs" + x[0], name)
# saluted_name = list(raw_saluted_name)
# print(saluted_name)

#  x = 0
#  y = 5
# if x or y:
#     print('yes')

# if 'foo' in ['foo', 'bar', 'baz']:
#     print('Outer condition is true')      

#     if 10 > 20:                           
#         print('Inner condition 1')        

#     print('Between inner conditions')    

#     if 10 < 20:                           
#         print('Inner condition 2')        

#     print('End of outer condition')       
# print('After outer condition')

# behaviour = input('input either good or bad:')
# age =int(input('enter your age:'))

# if behaviour == "good" and age < 18:
#     print('you get a car')
# if behaviour == "good" and age > 18:
#     print('you get a car')
# if behaviour == "bad":
#     print('GET OUT!!!!')


# score = int(input("what is your score?"))
# f = 'fail' if score< 50 else 'pass'
# print(f)

# health_status = str(input('answer with yes or no : ARE YOU OKAY?'))
# print(health_status)
# if health_status == 'yes':
#     print('Please get a life')
# else:
#     question_2= str(input('Do you have pains?'))
#     print(question_2)
#     if question_2== "no":
#         print('unable to diagnose')
    
#     else:
#         question = str(input('Did you sleep well?'))
#         print(question)
#     if question == 'no':
#         print('Try to sleep') 
#     else:
#         hardwork =str(input('have you done any hardwork?'))
#         print(hardwork)
#     if hardwork == 'no':
#         print('have some pain killer')
#     else:
#         fever = str(input('Do you have fever?'))
#         print(fever)
#     if fever == "yes":
#         print("inconclusive see a doctor?")
#     else:
#         vommiting = str(input('Are you vommiting?'))
#         print(vommiting)
#     if vommiting == 'yes':
#         print('see a doctor')
#     else:
#          print("Take some anti-malaria")

# saved_password = input('Please enter password :')
# if saved_password == "bolaji"
#     print('Welcome, correct password')
# else:
#     print('Incorrect password, pleas try again')
# qualified_income = 50000
# finiancial_status = input("What is your income per-month: ")
# if finiancial_status == "50000":
#     print('congratulation!!!, You are qualified to take a loan')
# if finiancial_status < '50000':
#     print('Sorry, you are not qualified to take a loan')
# else: 
#     print('congrats, you are qualified to borrow loan')

                                #LOOPS
# a = ['foo' , 'bar', 'baz']
# for i in a:
#     print(i)

# print("x".center(4), "|", "x-bar".center(7), "|", "(x-bar)**2".center(10), sep ="")
# print("____".center(4), "|", "_____".center(7), '|', '_________'.center(10),  sep = "")
# n = 7
# mean = sum(range(n))/len(range(n))
# for i in range(n):
#     print(f"{i}".center(4), "|", f"{i - mean}".center(7), "|", f"{(i - mean)**2}".center(10),  sep = "")

# names = ['john', 'clem']
# for i in names:
#     print('hello ' + i)

# vowels = ['a, e, i, o, u']
# word = input("please type in a word:")
# total_vowels = 0
# for vowel in vowels:
#     if vowel  in word:
#         print(vowel)
# word = input('please enter a word')
# for i in word:
#     print(i)
#     if i =="?":

#             break


# from sys import exit
# import random
# import time


# min = 1 
# max = 6 


# x = 0
# y = 0

# print
# player_name = input ("Abeg enter your name: ")
# print('Hw fa nah ' + player_name  + '?')
# Cap = player_name.upper()

# roll_again = "yes"

# while roll_again == "yes": 
#    if roll_again == "no":
#       exit(0)
#    print
#    print ("Your Turn")
#    print
#    time.sleep(1)
#    print ("the die dey roll, abeg wait...")
      
#    time.sleep (2)

#    x = random.randint(min, max)
#    y = random.randint(min, max)
 
#    def dice (m):
#      if m == 1:
#       print (""" 
#           _________
#          |         |
#          |         |  
#          |    *    | 
#          |         | 
#          |_________|  """)
         
#      elif m == 2:
#       print  ("""
#           _________
#          |         |
#          |     *   |
#          |         | 
#          |   *     | 
#          |_________|  """)
      
#      elif m == 3:
#       print ("""
#           _________
#          |         |
#          |      *  |  
#          |    *    | 
#          |  *      | 
#          |_________|  """) 
    
#      elif m == 4:
#       print ("""
#           _________
#          |         |
#          |  *   *  |  
#          |         | 
#          |  *   *  | 
#          |_________|  """) 
    
    
#      elif m == 5:
#       print (""" 
#           _________
#          |         |
#          |  *   *  |  
#          |    *    | 
#          |  *   *  | 
#          |_________|  """)
    
    
#      elif m == 6:
#       print ("""   
#           _________
#          |         |
#          |  *   *  |  
#          |  *   *  | 
#          |  *   *  | 
#          |_________|  """) 
   

#    dice (x)
   
#    print
#    time.sleep(1)
#    print
#    print ("Na d Computer's Turn")
#    time.sleep(1)
#    print
#    print ("Rolling the die")
#    time.sleep(2)
    
#    dice(y)
   
#    time.sleep(1)
   
   
#    # We set the condition of win, loss 
#    # and here.
   
#    if x == y:
#       print
#       print ("Ah! nah draw.")
#       time.sleep(1)
#       print
#       print ("abeg type 'yes' to play again or 'no' to stop playing.")
#       print
      
#    elif x > y:
#       print
#       print ("OSHEYY! You don Ama"), Cap
#       time.sleep(1)
#       print 
#       print ("u wan try again, type 'yes'. if u wan stop  playing, input 'no'.")
#       print
      
#    elif x < y:
#       print
#       print ("eyah! You Lost. Try again"), Cap
#       time.sleep(1)
#       print  
#       print ("To roll again, input 'yes'. To stop playing input 'no'.")
#       print
     
#    roll_again = input("Roll the die again?")
   
                                #    WHILE LOOPS
# n = 5
# for i in range(n):
#     n = n - 1
#     print(n) 
# x = 'boy toys junk'
# y = 'mum girls luck'
# n = 0 
# word_length = len (x)
# while n < word_length:
#     print(x[n], y[n]) 
#     n +=1 
#                     #   LIST; COMMON LIST METHOD
# mylist= [1,2,3,4,5]
# print(mylist)

# name = 'shalewa'
# mysecondlist = list(name)
# print(mysecondlist)

# products = 'shoes, bags, rings, shirts,'
# mythirdlist = (products).split(",")
# print(mythirdlist)                         

# # mythirdlist.append('shorts')
# attempts = 10
# while True:
#     already_counted = []
#     for item in mythirdlist:
#         if item not in already_counted:
#             occurences = mythirdlist.count(item)
#             already_counted.append(item)
#             print(item, occurences)

#     action = input('what would like to do: ')
    
#     if action == 'add':
#         # add to list
#         new_prop = input('enter a new prop:')
#         mythirdlist.append(new_prop)
#         print(mythirdlist)
        
#     elif action == 'rem':
#         # remove from list
#         new_prop = input('enter a new prop to remove:')
#         mythirdlist.remove(new_prop)
#         # print(mythirdlist)
#     attempts -=1
    
#     if attempts == 0:
#         print('you have run out of attempts!!!!')
#         break  


# import random 
# random_nums = []

# for i in range(20):
#     rand_num = random.randint(1,7)
#     random_nums.append(rand_num)
# print(random_nums)

# already_counted = []
# for item in random_nums:
#     if item not in already_counted:
#         occurences = random_nums.count(item)
#         # already_counted.append(item)
#         print(item, occurences)
                        
#                         # DICTIONARY
# name = input('what is your name?')
# age = input('how old are you? : ')
# gender = input('what is your gender : ')
# first_dict = {'name':name, 'age': age, 'sex': gender}
# print(first_dict['name'].upper(),"is", first_dict['age'].upper(), "and is a", first_dict['sex'].upper()) 
# first_dict["courses"] = ""
# print(first_dict)
# del first_dict['name of key'] TO DELETE FROM DICTIONARY
#                                         # ANOTHER WAY TO CREATE A DICTIONARY
# new_dict = dict((('name', 'bolaji'), ('age', 14), ('years', 1) ))           

                        # CLASSWRK
# songchoice = input('what song would you like to listen to? (type either risky or perfect): ')
# if songchoice == 'perfect':
#     perfect_file = open("perfect_lyrics.txt", "r")

#     data = perfect_file.readlines()
#     lyrics_dict = {}
#     line_num = 1

# if songchoice == 'risky':
#     risky_file = open("risky lyrics.txt", "r")
#     data = risky_file.readlines()
#     lyrics_dict = {}
#     line_num = 1


#for line in data:
#     lyrics_dict[line_num] = line
#     line_num+=1

# # print(lyrics_dict)

# while True:
#     requested_line = int(input('what line would you like to get: '))
#     print(lyrics_dict[requested_line])
                                        # CORRECTION
# risky = "risky lyrics"
# perfect = "perfect_lyrics"
# file = open(f"{risky}.txt", "r")

# data = file.readlines()
# lyrics_dict = {}
# line_num = 1
# lyrics_dict[risky] = {}

# for line in data:
#     lyrics_dict[risky][line_num] = line
#     line_num+=1
# file.close()

# file = open(f"{perfect}.txt", 'r')

# data = file.readlines()
# line_num = 1
# lyrics_dict[perfect] = {}
# for line in data:
#     lyrics_dict[perfect][line_num] = line 
#     line_num+=1
# file.close()
# print(lyrics_dict.keys())

# while True:
#     requested_song = input('please what song would you like to get')
#     print(lyrics_dict.keys())
#     requested_line = int(input('please what line would like to get:'))
#     print(lyrics_dict[requested_song])

# import requests 
# # import matplotlib.pyplot as plt
# url = "http://checklight.pythonanywhere.com/streets"
# response = requests.get(url)
# data = response.json()
# # print(data.keys())

# # print(type(data["streets"]))

# streets =  data["streets"]

# for street in streets:
    # print(street.get('name').center(20),'|', street.get('last-no-light').center(20),'|', (street.get('status')).center(4))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    # print(street.get('history').get('time_line'))
    # print('\n', street.get("name").center(20),'-',street.get('last_no_light').center(20),'-',street.get('lga').center(20))

    # print("\n\t--------------TIMELINES------------\n")
    # timelines = street.get("history").get("time_line")
    # for timeline in timelines:
    #     status = "up nepa" if timeline.get('status') == 1 else 'down nepa'
    #     period = round(timeline.get('period')/3600, 1)
    #     time = timeline.get('time')
    #     print("\t", str(time).center(12), str(period)+('hours').center(12), str(status).center(12), sep = "|")

        # TO PLOT A GRAPH IN PYTHON; first "import matplotlib.pyplot" as plt like in line 565   
    # daily_supply = street.get("history").get("daily_supply")
    # print(daily_supply)

    # labels = daily_supply['labels']
    # values =daily_supply["values"]

    # plt.bar(labels, values)
    # plt.title(street.get('name'))
    # plt.show()
# import requests    
# devices = ['lx0d001','lx0d002', 'lx0d003', 'lx0d004' ]    
# all_devices = {}

# for device in devices: 
#     url = f"http://checklight.pythonanywhere.com/get_readings/{device}/12/"
#     response = requests.get(url)
#     data = response.json()

#     streets =  data["streets"]
    
#     days = {}

#     for street in streets:
#         status = street["status"]



#         time = street["time"]
#         day = time[5:7]

#         if status == 0:
#             if day not in days:
#                 days[day] = 0
#             days[day] +=1
#     all_devices[device] = days

# # print(days) 
# print(all_devices)

# import citylist
# import requests
# import time
# import datetime

# cities = citylist.citylist

# requested_city = input("Please enter city in check \n:").lower()

# for city in cities:
#     if requested_city in city['name'].lower():
#         print(city["name"], city["coountry"])
# requested_country = input('please enter country code \n:').lower()

# for city in cities:
#     if requested_city in city["name"].lower() 


#                                       FUNCTIONS
# def dumb_func(x,y):
#     print(x)
#     print(y)
#     return x - y
# def dumb_func_add(x,y):
#     return x + y
# result = dumb_func(2,6)
# print(result)
# jfkg = dumb_func_add(2,6)
# print(jfkg)
#                     #       simple interests: classwork
# principal = int(input('Enter your principal;'))
# rate = int(input('Enter your rate:'))
# Time = int(input('enter period of payment:'))
# def simple_interests(P,R,T):
#     interests = (P * R * T)/100

#     return interests
# print(simple_interests(principal, rate, Time))

# def factorial_iter(n):
#     num = 1
#     while n >= 1:
#         num = num*n
#         print(num)
#         n = n-1
#     return num
# print(factorial_iter(5))

# empty_list = []
# def factorial_iter(n):
#     num = 1 
#     num = num * n
#     empty_list.apend(str(n))
#     n = n-1
# print("x".join(empty_list),"=",num )
                    # CLASSWORK
# empty = []
# def fibonacci(n):
#     first_num = 1
#     for i in range(1,10):
#         i = ((first_num +i ) )
#         fibon = first_num + i
#         empty.append(str(fibon))
#     return empty
# print(fibonacci(10))

    # CORRECTION
# def fib_seq(n):
#     seq = []

#     for i in range(n):
#         if len(seq) < 2:
#             seq.append(i)
#         else:
#             new_sequence = seq[i-1] + seq [1-2]
#             seq.append(new_sequence)
#     print(seq)

# fib_seq(22)
# def fib_seq_v2(first_num, second_num, quantity ):
#     seq = [first_num, second_num]
#     for i in range in (quantity):

#             new_sequence = seq[i-1] + seq[i-2]
#             seq.append(new_sequence)
#     print(seq)
# fib_seq_v2(1,1,22) 

#                 # VARIANCE: ASSIGNMENT WEEK 7
# import random
# random_list1 = []
# random_list2 = []
# def gen_and_list(j):
#     for rand_num in range(10):
#         rand_num = random.randint(1,10)
#         random_list1.append(rand_num)
#     return random_list1

# statement = f'first random list is = {gen_and_list(10)}'

# print(statement)

# def gen_in_list2(i):
#     for num in range(10):
#         num = random.randint(1,10)
#         random_list2.append(num)
#     return random_list2
# print (f'second random list is = {gen_in_list2(10)}')
# def mean(mean):
#     meanone = sum(random_list1)/len(random_list1)
#     second = sum(random_list2)/len(random_list2)
#     # return first_mean
#     # return second_mean
#     return (f'first mean is : {meanone}, second mean is : {second}')
# print(mean(10))

# def variance(v):
#     first_list = (sum(random_list1)**2)/(len(random_list1)-1)
#     second_list = (sum(random_list2)**2)/(len(random_list2)-1)
#     return (f' first variance =  {first_list}, second variance = {second_list}' )
# print(variance(10))


# x_bar = [i - mean for i in ]
# pearson_colleration = (sum(x_bar)/ ((sum(x_bar)**2))**0.5) 

# # ######################PEARSON CORRELATION
# def pearson_correlation(x, y):
#     pearson_formula = random_list1 + random_list2 + str(firstbar= int(random_list1 -  mean)) + (random_list2 - mean) + 'firstbar'
#     return pearson_formula

                     # *args & Kwargs
# def my_func(*names):
#     print(names)

# data = ['atha', 'deji', 'tunji']
# my_func(*data)

# def bio (name, age, gender):
#     print("name:", name, "age:", age,"gender :", gender)
# # bio("atha", "male",28) #positional argument
# # bio(name = "atha", gender = "male", age = 28)    #KEYWORD ARGUMENT

#                 # RECURSION
# def printer(n):
#     print(n)
#     if n == 0:
#         print("base case was met!!!!")
#         return
#     n = n-1
#     return printer(n)
# printer(3)                
            
            
#         # HOW TO SEND A REQUEST TO AN API
# import requests

# data = {"username": "dtekluva", "data": [{"name":"tolu","age": 30, "class": 5}, {"name":"tolu", "age": 30, "class":5},]}

# url = "http://theapiaddress"
# response = requests.post(url, data)
# print(response.json())

# import requests
# import json
# login_details = {
#     "username"   :  "bolajibot",
#     "firstname"  :  "Mobolaji",
#     "lastname"   :  "Akisanya",
#     "email"      :  "akisanyamobolaji@gmail.com",
#     "phone"      :  "08179414846",
#     "details"    :  "Welcome to my world!!!",
#     "password"   :  "olatunbosun"
# }

# json_data = json.dumps(login_details)
# url = "http://univelcity.pythonanywhere.com/data/register/"
# req = requests.post(url, json_data)


# print(req.json())


# import requests
# import json


# Billionaire = "Billionaire -- Teni.lrc"
# Blowmymind = "Blow My Mind -- Davido.lrc"
# By_you = "By You -- simi.lrc"
# Dumebi = "Dumebi -- Rema.lrc"
# Elastic = 'Elastic Heart -- Sia.lrc'
# fall = 'Fall -- davido.lrc'
# love_yourself = 'Love Yourself -- Justin Bieber.lrc'
# Mirrors = 'Mirrors Justin-- Timberlake.lrc'
# Perfect = 'Perfect -- Ed sheeran.lrc'
# smile = 'Smile For Me -- Simi,lrc'
# stay = 'Stay -- Rihanna.lrc'

# url = 'http://univelcity.pythonanywhere.com/data/add_lyrics/'
# lyrics_list = [Billionaire, Blowmymind, By_you, Dumebi, Elastic, fall, love_yourself, Mirrors, Perfect, smile, stay]

# username : 'bolajibot'
# IRBW_2_XaKhMeWimMfcANccVoL2_2Nc6poYV5QXkO8CydmbUv4GZmg : lyrics_list


# req = requests.post(url, lyrics_list)


# print(req.json())










# Billionaire = "Billionaire -- Teni.lrc"
# Blowmymind = "Blow My Mind -- Davido.lrc"
# By_you = "By You -- simi.lrc"
# Dumebi = "Dumebi -- Rema.lrc"
# Elastic = 'Elastic Heart -- Sia.lrc'
# fall = 'Fall -- davido.lrc'
# love_yourself = 'Love Yourself -- Justin Bieber.lrc'
# Mirrors = 'Mirrors Justin-- Timberlake.lrc'
# Perfect = 'Perfect -- Ed sheeran.lrc'
# smile = 'Smile For Me -- Simi,lrc'
# stay = 'Stay -- Rihanna.lrc'

# lyrics1 = open(Billionaire, "r")
# data1 = lyrics1.readlines()
# word = str(Billionaire)
# vowels = ['a','e','i','o','u']
# total_vowels = 0


# print(f"Vowels | Count")
# print(f"_______|_______")
# for i in vowels:
#     if i in word:
#         # print(i)
#         count = word.count(i)
#         total_vowels = total_vowels + count
#         print(f"{i.center(6)} | {str(count).center(6)}")
# print(f"Total vowels: {total_vowels}")
# lyrics2 = open(Blowmymind, "r")
# data2 = lyrics2.readlines()
# lyrics3 = open(By_you, "r")
# data3 = lyrics3.readlines()
# lyrics4 = open(Dumebi, "r")
# data4 = lyrics4.readlines()
# lyrics5 = open(Elastic, "r")
# data5 = lyrics5.readlines()
# lyrics6 = open(fall, "r")
# data6 = lyrics6.readlines()
# lyrics7 = open(love_yourself, "r")
# data7 = lyrics7.readlines()
# lyrics8 = open(Mirrors, "r")
# data8 = lyrics8.readlines()
# lyrics9 = open(Perfect, "r")
# data9 = lyrics9.readlines()
# lyrics10 = open(smile, "r")
# data10 = lyrics10.readlines()
# lyrics11 = open(stay, "r")
# data11 = lyrics11.readlines()












############################Most occurring word in lyrics
########################### Vowel count in lyrics


#ACESS TOKEN :  IRBW_2_XaKhMeWimMfcANccVoL2_2Nc6poYV5QXkO8CydmbUv4GZmg


###################################################################      OOP

# ############# CLASSES################
# class Animal:
#     def talk(self):
#         print("i have something to say!")
#     def walk(self):
#         print("hey! i am walking here!")
#     def clothes(self):
#         print("i have nice clothes")
        
# animal = Animal()
# animal.talk()
# animal.clothes()
# animal.walk()


# class account:
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


################################## CLW
import pymysql.cursors

connection = pymysql.connect(host = 'localhost',
                            user = 'root',
                            password = '',
                            db = 'my_db',
                            charset = 'utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


with connection.cursor() as cursor:
    import random 

    names = open('random_names.txt', 'r').read()
    emails = ['@gmail.com', '@yahoo.com', '@live.com']
    splitted_names = names.splitlines()
    for name in splitted_names:
        fname, lname = name.split()
        random_email = random.choice(emails)
        email = f"{fname[:3]}{lname[:3]}{random_email}"
        age = random.randint(10, 50)
        salary = random.randint(100000, 500000)
        print(f"firstname -  {fname},  lastname -  {lname},  Age -  {age},  email-  {email},  salary - {salary}")
        sql_cmd = f'INSERT into person (fname, lname, age, address,email, salary) values ("{fname}", "{lname}", {age} ,"abuja",  "{email}", "{salary}")'
        
        cursor.execute(sql_cmd)
        connection.commit()
# print(splitted_names)
