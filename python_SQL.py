import pymysql.cursors

connection = pymysql.connect(host = 'localhost',
                            user = 'root',
                            password = '',
                            db = 'my_db',
                            charset = 'utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

############################################ INSERT SINGLE USER
with connection.cursor() as cursor:
    #create a new record
    sql_cmd = 'INSERT into student (f_name, l_name, age, address,email, salary) values ("ola", "hish", 26, "yaba, lagos", "bj@gmail.com", 600000)'

    cursor.execute(sql_cmd)
    connection.commit()
print(sql_cmd)