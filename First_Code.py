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

# file = open("my_data.csv", 'a')
# print("name","age","state","due", file = file,sep =",")
# print("ade","20","osun_state","20000", file = file,sep =",")

# file = open("my_data.csv", 'a')
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