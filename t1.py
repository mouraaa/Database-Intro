import psycopg2
from tabulate import tabulate

try:
	#connect to the database
	connect = psycopg2.connect(
			host = '127.0.0.1', 
			database = 'name_of_database', 
			user = 'postgres', 
			password = 'postgres_password')

	#create a cursor object to use queries
	cursor = connect.cursor()

	#execute queries
	# cursor.execute('drop table t1;')
	cursor.execute('create table t1(name varchar(10), age int);')

	while True:
		name = input("Please enter the user's first name: ")
		age = input(f'How old is {name}: ')
		cursor.execute('Insert into t1(name,age) values (%s, %s);', (name, int(age)))
		answer = input("Do you have anyone else to add? [y/n]: ")
		if answer == 'y' or answer == 'yes':
			continue
		elif answer == 'n' or answer == 'no':
			break
		else:
			print("Invalid entry. Please try again")

	cursor.execute('Select * from t1;')
	records = cursor.fetchall()
	#print with table
	print(tabulate(records, headers=['Name', 'Age'], tablefmt='psql')) 

	#print without table
	# print("AGE:            NAME:")
	# print('---------------------')
	# for r in records:
	# 	print(f'AGE: {r[0]}        NAME: {r[1]}' ) 

except:
	print("Something went wrong while connecting or querying the database")

finally:
	connect.commit() 
	cursor.close()
	connect.close()