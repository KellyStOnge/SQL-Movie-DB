import sys
import os
import mysql.connector
from mysql.connector import errorcode
import csv
import json
from csv import reader


file = sys.argv[1:] #the file


DB_NAME = 'moviedbtest' #movie db

TABLES = {}

TABLES['movies'] = (
    "CREATE TABLE `movies` ("
    "  `id` varchar(6) NOT NULL,"
    "  `budget` varchar(50) NOT NULL,"
    "  `homepage` varchar(250) NOT NULL,"
    "  `original_language` varchar(2) NOT NULL,"
    "  `original_title` varchar(100) NOT NULL,"             #building the db frame
    "  `overview` varchar(1500) NOT NULL,"
    "  `popularity` varchar(15) NOT NULL,"
    "  `release_date` varchar(20) NOT NULL,"
    "  `revenue` varchar(15) NOT NULL,"
    "  `runtime` varchar(10) NOT NULL,"
    "  `status` varchar(50) NOT NULL,"
    "  `tagline` varchar(500) NOT NULL,"
    "  `title` varchar(100) NOT NULL,"
    "  `vote_average` varchar(50) NOT NULL,"
    "  `vote_count` varchar(15) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['genres'] = (
    "CREATE TABLE `genres` ("
    "  `id` int(4) NOT NULL,"
    "  `name` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['movie_genres'] = (
    "CREATE TABLE `movie_genres` ("
    "  `unique_id` varchar(7)NOT NULL,"
    "  `movie_id` varchar(6) NOT NULL,"
    "  `genre_id` varchar(6) NOT NULL,"
    "  PRIMARY KEY (`unique_id`)"
    ") ENGINE=InnoDB")

TABLES['keywords'] = (
    "CREATE TABLE `keywords` ("
    "  `id` int(4) NOT NULL,"
    "  `name` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['movie_keywords'] = (
    "CREATE TABLE `movie_keywords` ("
    "  `unique_id` varchar(7)NOT NULL,"
    "  `movie_id` varchar(6) NOT NULL,"
    "  `keywords_id` varchar(4) NOT NULL,"
    "  PRIMARY KEY (`unique_id`)"
    ") ENGINE=InnoDB")

TABLES['production_companies'] = (
    "CREATE TABLE `production_companies` ("
    "  `id` int(4) NOT NULL,"
    "  `name` varchar(60) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['movie_production_companies'] = (
    "CREATE TABLE `movie_production_companies` ("
    "  `unique_id` varchar(7)NOT NULL,"
    "  `movie_id` varchar(6) NOT NULL,"
    "  `comp_id` varchar(4) NOT NULL,"
    "  PRIMARY KEY (`unique_id`)"
    ") ENGINE=InnoDB")

TABLES['production_countries'] = (
    "CREATE TABLE `production_countries` ("
    "  `id` varchar(7) NOT NULL,"
    "  `name` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['movie_production_countries'] = (
    "CREATE TABLE `movie_production_countries` ("
    "  `unique_id` varchar(7)NOT NULL,"
    "  `movie_id` varchar(6) NOT NULL,"
    "  `country` varchar(2) NOT NULL,"
    "  PRIMARY KEY (`unique_id`)"
    ") ENGINE=InnoDB")

TABLES['spoken_languages'] = (
    "CREATE TABLE `spoken_languages` ("
    "  `id` varchar(2) NOT NULL,"
    "  `name` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['movie_spoken_languages'] = (
    "CREATE TABLE `movie_spoken_languages` ("
    "  `unique_id` varchar(7)NOT NULL,"
    "  `movie_id` varchar(6) NOT NULL,"
    "  `language` varchar(2) NOT NULL,"
    "  PRIMARY KEY (`unique_id`)"
    ") ENGINE=InnoDB")


cnx = mysql.connector.connect(user='root', password='password') # connector
cursor = cnx.cursor()




def create_database(cursor):

    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME)) # committing the db to MYSQL
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME)) #checks to see if the DB is there
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
        
    table_description = TABLES[table_name]

    try:
        print("Creating table {}: ".format(table_name), end='') ##checks to see if the table is there
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()

cnx = mysql.connector.connect(user='root', database='moviedbtest', password ='password')
cursor = cnx.cursor()


with open(sys.argv[1], 'r') as read_obj: # insert data

    csv_reader = reader(read_obj) # open the file
    next(csv_reader, None)
    ii =0
    jj =0
    kk =0 # counters
    cc =0
    dd =0 


    for row in csv_reader:

        cnx = mysql.connector.connect(user='root', database='moviedbtest', password ='password') #connect the conector
        cursor = cnx.cursor()

        print("\n",row[0]) # budget the first row 
        budget = row[0]
        
        
        keywordss=json.loads(row[1]) # json loads builds a literal string into a dictionary to access

        lst = str(row[1])

        j = 0

        for i in keywordss:  # break the genres apart 

            if lst == '[]': # if theres nothing skip
                break

            new_id = keywordss[j]['id'] # grab id
            
            new_keyword = keywordss[j]['name'] # grab name 
            movie_name_id =row[3] # grab the movie id

            add_genre = ("INSERT INTO genres "
                               "(id, name) "
                               "VALUES (%s, %s)") # insert into genres


            data_genre = (new_id, new_keyword)

            

            try:

                    cursor.execute(add_genre,data_genre) #if this doesnt exist create it 
                    
                    cnx.commit()
                    cursor.close()
                    cnx.close() 
                    j+=1
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY: # if it does exist skip
                    print("already exists.")
                    j+=1
                    continue




        keywords2=json.loads(row[1])


        lst = str(row[1])

        z = 0
        
        for x in keywords2:

            cnx = mysql.connector.connect(user='root', database='moviedbtest', password ='password')
            cursor = cnx.cursor()

            ii +=1

            if lst == '[]':
                break

            the_id = keywords2[z]['id']
            
            movie_name_id =row[3]

        

            add_ids = ("INSERT INTO movie_genres "
                               "(unique_id,movie_id, genre_id) "
                               "VALUES (%s, %s, %s)")

           

            movie_genre_ids = (ii,movie_name_id,the_id)


            try:

                    cursor.execute(add_ids,movie_genre_ids)
                    cnx.commit()
                    cursor.close()
                    cnx.close() 
                    z+=1
                    
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    print("already exists.")
                    z+=1
                    
                    continue
                
            

        keywordss=json.loads(row[4])

        lst = str(row[4])

        j = 0


        for i in keywordss:

            if lst == '[]':
                break

            new_id = keywordss[j]['id']
            new_keyword = keywordss[j]['name']


            add_genre = ("INSERT INTO keywords "
                               "(id, name) "
                               "VALUES (%s, %s)")

            data_genre = (new_id, new_keyword)

            try:

                    cursor.execute(add_genre,data_genre)
                    cnx.commit()
                    cursor.close()
                    cnx.close() 
                    j+=1
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    print("already exists.")
                    j+=1
                    continue



        key_keywordss=json.loads(row[4])


        lst = str(row[4])

        f = 0

        j = 0


        for v in key_keywordss:

            cnx = mysql.connector.connect(user='root', database='moviedbtest', password ='password')
            cursor = cnx.cursor()

            jj +=1

            if lst == '[]':
                break

            the_key_id = key_keywordss[f]['id']
            
            movie_name_id = row[3]



            add_key_ids = ("INSERT INTO movie_keywords "
                                 "(unique_id,movie_id,keywords_id) "
                                 "VALUES (%s, %s, %s)")

            

            movie_key_ids = (jj,movie_name_id,the_key_id)


            try:

                    cursor.execute(add_key_ids,movie_key_ids)
                    cnx.commit()
                    cursor.close()
                    cnx.close() 
                    f+=1
                    
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    print("already exists.")
                    f+=1
                    
                    continue


        keywordss=json.loads(row[9])

        lst = str(row[9])

        j = 0

        for i in keywordss:

            if lst == '[]':
                break

            new_id = keywordss[j]['id']
            new_keyword = keywordss[j]['name']

            add_genre = ("INSERT INTO production_companies "
                               "(id, name) "
                               "VALUES (%s, %s)")

            data_genre = (new_id, new_keyword)

            try:

                    cursor.execute(add_genre,data_genre)
                    cnx.commit()
                    cursor.close()
                    cnx.close() 
                    j+=1
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    print("already exists.")
                    j+=1
                    continue


        key_production=json.loads(row[9])


        lst = str(row[9])

        a = 0

        j = 0


        for l in key_production:

            cnx = mysql.connector.connect(user='root', database='moviedbtest', password ='password')
            cursor = cnx.cursor()

            kk +=1

            if lst == '[]':
                break

            the_p_id = key_production[a]['id']
            
            movie_name_id = row[3]

            print("AAA:",a)

            print(kk)
            print(the_p_id)
            print(movie_name_id)

            add_p_ids = ("INSERT INTO movie_production_companies "
                                 "(unique_id,movie_id,comp_id) "
                                 "VALUES (%s, %s, %s)")

            

            movie_p_ids = (kk,movie_name_id,the_p_id)

            print(movie_p_ids)


            try:

                    cursor.execute(add_p_ids,movie_p_ids)
                    cnx.commit()
                    cursor.close()
                    cnx.close() 
                    a+=1
                    
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    print("already exists.")
                    a+=1
                    
                    continue


        keywordss=json.loads(row[10])

        lst = str(row[10])

        j = 0

        for i in keywordss:

            if lst == '[]':
                break

            new_id = keywordss[j]['iso_3166_1']
            new_keyword = keywordss[j]['name']

            add_genre = ("INSERT INTO production_countries "
                               "(id, name) "
                               "VALUES (%s, %s)")

            data_genre = (new_id, new_keyword)

            try:

                    cursor.execute(add_genre,data_genre)
                    cnx.commit()
                    cursor.close()
                    cnx.close() 
                    j+=1
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    print("already exists.")
                    j+=1
                    continue

        key_countries=json.loads(row[10])

        print(key_production)

        lst = str(row[10])

        b = 0

        j = 0



        for l in key_countries:

            cnx = mysql.connector.connect(user='root', database='moviedbtest', password ='password')
            cursor = cnx.cursor()

            cc +=1

            if lst == '[]':
                break

            the_c_id = key_countries[b]['iso_3166_1']
            
            movie_name_id = row[3]


            add_c_ids = ("INSERT INTO movie_production_countries "
                                 "(unique_id,movie_id,country) "
                                 "VALUES (%s, %s, %s)")

            

            movie_c_ids = (cc,movie_name_id,the_c_id)



            try:

                    cursor.execute(add_c_ids,movie_c_ids)
                    cnx.commit()
                    cursor.close()
                    cnx.close() 
                    b+=1
                    
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    print("already exists.")
                    b+=1
                    
                    continue



        keywordss=json.loads(row[14])

        lst = str(row[14])

        j = 0

        for i in keywordss:

            if lst == '[]':
                break

            new_id = keywordss[j]['iso_639_1']
            new_keyword = keywordss[j]['name']

            add_genre = ("INSERT INTO spoken_languages "
                               "(id, name) "
                               "VALUES (%s, %s)")

            data_genre = (new_id, new_keyword)

            try:

                    cursor.execute(add_genre,data_genre)
                    cnx.commit()
                    cursor.close()
                    cnx.close() 
                    j+=1
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    print("already exists.")
                    j+=1
                    continue

        key_spoken=json.loads(row[14])

       

        lst = str(row[14])

        o = 0

        j = 0


        for n in key_spoken:

            cnx = mysql.connector.connect(user='root', database='moviedbtest', password ='password')
            cursor = cnx.cursor()

            dd +=1

            if lst == '[]':
                break

            the_s_id = key_spoken[o]['iso_639_1']
            
            movie_name_id = row[3]


            add_s_ids = ("INSERT INTO movie_spoken_languages "
                                 "(unique_id,movie_id,language) "
                                 "VALUES (%s, %s, %s)")

            

            movie_s_ids = (dd,movie_name_id,the_s_id)


            try:

                    cursor.execute(add_s_ids,movie_s_ids)
                    cnx.commit()
                    cursor.close()
                    cnx.close() 
                    o+=1
                    
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    print("already exists.")
                    o+=1
                    
                    continue




csv_dict = csv.DictReader(open(sys.argv[1], 'r')) # ALOT OF THESE ABOVE DO THE SAME SEPERATING VALUES AND THEN PUTING THE 

#                                                    # DB into 3NF .. THIS BELOW TAKES CARE OF THE REST

count = 0
for row in csv_dict:

    cnx = mysql.connector.connect(user='root', database='moviedbtest', password ='password')
    cursor = cnx.cursor()

    
    budget = row['budget']
    movie_id = row['id']
    homepage = row['homepage']
    original_lan = row['original_language']
    original_tit = row['original_title']
    overview =row['overview']
    popularity = row['popularity']
    release_date = row['release_date']
    revenue = row['revenue']
    runtime = row['runtime']
    status = row['status']
    tagline = row['tagline']
    title = row['title']
    vote = row['vote_average']
    vote_count = row['vote_count']


    


    print(row['budget'],row['id'],row['title'])


    add_movie = ("INSERT INTO movies "
               "(id, budget,homepage,original_language,original_title,overview,popularity,release_date,revenue,runtime,status,tagline,title,vote_average,vote_count) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )")



    data_movie = (movie_id,budget,homepage, original_lan, original_tit, overview, popularity, release_date, revenue, runtime, status , tagline, title, vote,vote_count)



    try:
        cursor.execute(add_movie,data_movie)
        cnx.commit()
        cursor.close()
        cnx.close() 
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DUP_ENTRY:
            print("already exists.")




print("DONE!")



