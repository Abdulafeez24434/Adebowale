import pymysql.cursors


connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db='my_db',
                             charset = 'utf8mb4',
                             cursorclass =pymysql.cursors.DictCursor)

# with connection.cursor() as cursor:
#     sql_cmd = 'INSERT into person (FNAME,Iname,age,address,email,salary) values ("ariri","joe","15","sabo","aririjoseph@gmail.com",5000000)'
#     cursor.execute(sql_cmd)
#     connection.commit()
#     print("done")



import random
with connection.cursor() as cursor:
    data = open("randomnames.txt","r")
    names = data.read()
    splitted_names = names.splitlines()
    emails = ["@gmail.com", "@yahoo.com", "@live.com"]
    for name in splitted_names:
        print(name)
        fname, Iname = name.split()[0], name.split()[1]
        random_email = random.choice(emails)
        email = f"{fname[:3]}{Iname[:3]}{random_email}"
        age = random.randint(10,50)
        salary = random.randint(100000,10000000)
        print(f"first name = { fname}, lastname = {Iname}, age = {age}, email = {email},salary={salary}")
        sql_cmd = f'INSERT into person (FNAME,Iname,age,address,email,salary) values ("{fname}","{Iname}","{age}","abuja","{email}","{salary}")'

        cursor.execute(sql_cmd)
        connection.commit()
        print("done")









