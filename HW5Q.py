import mysql.connector
import os
import sys

# database connection
connection = mysql.connector.connect(
	host="localhost", user="root", 
	  password="password", database="moviedbtest")
cursor = connection.cursor()


print("Homework 5 movie queries")


while True:
	
	print("Enter one of the following options: q1, q2, q3, q4, q5, or quit")
	option = input("> ")

	# Check the user input and execute the appropriate code
	if option == "q1":

		connection = mysql.connector.connect(
		host="localhost", user="root", 
	  	password="password", database="moviedbtest")
		cursor = connection.cursor()

		print("\n")
		print("Q1: What is the average budget of all movies? Your output should include just the average budget value.\n")
		
		avg_budget = "Select AVG(budget) AS average from movies;"

		cursor.execute(avg_budget)
		rows = cursor.fetchall()
		for i in rows:
			print(str(i[0]))
		  
		  

		connection.commit()
		connection.close()

		print("\n")


		#29045039.87528628
		

	elif option == "q2":
		connection = mysql.connector.connect(
		host="localhost", user="root", 
	  	password="password", database="moviedbtest")
		cursor = connection.cursor()

		print("\n")
		print("Show the movies that were produced in the United States. Your output must include the movie title and the production company name.\n")


		US_Movies = "SELECT \
		 movies.original_title AS movie_title, \
		 production_companies.name AS company_name \
		 from movies \
		 LEFT JOIN movie_production_companies ON movies.id = movie_production_companies.movie_id \
		 LEFT JOIN movie_production_countries ON movies.id = movie_production_countries.movie_id \
		 LEFT JOIN production_companies ON movie_production_companies.comp_id = production_companies.id  \
		 WHERE movie_production_countries.country ='US'"
		 #limit 25;" 
  

		cursor.execute(US_Movies)
		rows = cursor.fetchall()
		for row in rows:
			movie_title = row[0]
			company_name = row[1]
			print(f"{movie_title} ({company_name})")
		  
		connection.commit()
		connection.close()

		print("\n")

	elif option == "q3":

		connection = mysql.connector.connect(
		host="localhost", user="root", 
	  	password="password", database="moviedbtest")
		cursor = connection.cursor()



		print("\n")
		print("Show the top 5 movies that made the most revenue. Your output must include the movie title and how much revenue it brought in.\n")



		top_rev = "SELECT original_title, revenue FROM movies ORDER BY revenue DESC LIMIT 5"

		cursor.execute(top_rev)
		rows = cursor.fetchall()
		for row in rows:
		    movie_title = row[0]
		    revenue = row[1]
		    print(f"{movie_title}: {revenue}")
		  
		connection.commit()
		connection.close()

		print('\n')

	elif option == "q4":

		connection = mysql.connector.connect(
		host="localhost", user="root", 
	  	password="password", database="moviedbtest")
		cursor = connection.cursor()


		print("\n")
		print("What movies have both the genre Science Fiction and Mystery? Your output must include the movie title and all genres associated with that movie.\n")


		scifi_mys = "SELECT movies.original_title AS title, GROUP_CONCAT(genres.name) AS genres \
             FROM movies \
             LEFT JOIN movie_genres ON movies.id = movie_genres.movie_id \
             LEFT JOIN genres ON movie_genres.genre_id = genres.id \
             WHERE genres.name IN ('Science Fiction', 'Mystery') \
             GROUP BY movies.id \
             HAVING COUNT(DISTINCT genres.name) = 2 \
             LIMIT 5"

		cursor.execute(scifi_mys)
		rows = cursor.fetchall()
		for row in rows:
		    title = row[0]
		    genres = row[1]
		    print(f"{title}: {genres}")
			
		connection.commit()
		connection.close()

		print("\n")

		# Cypher: Science Fiction,Mystery
		# Congo: Mystery,Science Fiction
		# Halloween III: Season of the Witch: Mystery,Science Fiction
		# The Thirteenth Floor: Science Fiction,Mystery
		# The Thing: Mystery,Science Fiction
		

	elif option == "q5":

		connection = mysql.connector.connect(
		host="localhost", user="root", 
	  	password="password", database="moviedbtest")
		cursor = connection.cursor()


		print("\n")
		print("Find the movies that have a popularity greater than the average popularity. Your output must include the movie title and their popularity\n")


		pop = "SELECT original_title, popularity FROM movies WHERE popularity > (SELECT AVG(popularity) FROM movies) LIMIT 5"

		cursor.execute(pop)
		rows = cursor.fetchall()
		for i in rows:
		    print(f"Movie title: {i[0]}, Popularity: {i[1]}")

		connection.commit()
		connection.close()

		print("\n")

		# Movie title: Dumb and Dumber To, Popularity: 67.767785
		# Movie title: A Nightmare on Elm Street Part 2: Freddy's Revenge, Popularity: 21.607228
		# Movie title: The Pacifier, Popularity: 35.4763
		# Movie title: My Sister's Keeper, Popularity: 24.09152
		# Movie title: I, Frankenstein, Popularity: 31.324734

	elif option == "quit":
		print("Exiting program...LE FIN")
		sys.exit()
	

	else:
		print("Invalid option, please try again.")

