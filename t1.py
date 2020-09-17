import psycopg2
from tabulate import tabulate

try:
	#connect to the database
	connect = psycopg2.connect(
			host = '127.0.0.1', 
			database = 'name_of_your_database', 
			user = 'postgres', 
			password = 'postegre_password')

	#create a cursor object to use queries
	cursor = connect.cursor()

	#execute queries
	cursor.execute('create table t1(id int, name varchar(10));')

	while True:
		name = input("Please enter the user's first name: ")
		age = input(f'How old is {name}: ')
		cursor.execute('Insert into t1(id,name) values (%s, %s);', (int(age), name))
		answer = input("Do you have anyone else to add? [y/n]")
		if answer == 'y' or answer == 'yes':
			continue
		elif answer == 'n' or answer == 'no':
			break
		else:
			print("Invalid entry. Please try again")

	cursor.execute('Select * from t1;')
	records = cursor.fetchall()
	print(tabulate(records, headers=['ID', 'Name'], tablefmt='psql')) 

except:
	print("Something went wrong while connecting or quering the database")

finally:
	connect.commit() 
	cursor.close()
	connect.close()