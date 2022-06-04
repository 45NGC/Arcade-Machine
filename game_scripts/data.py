import sqlite3

def create_database():
	try:
		query = '''CREATE TABLE IF NOT EXISTS `users` (
                                      `id` INTEGER PRIMARY KEY AUTOINCREMENT,
                                      `username` VARCHAR(25) NOT NULL,
                                      `password` VARCHAR(25) NOT NULL,
                                      `tetris_record1` INT(15),
                                      `tetris_record2` INT(15),
                                      `tetris_record3` INT(15),
                                      `tetris_record4` INT(15),
                                      `tetris_record5` INT(15)
                                  );'''

		sqliteConnection = sqlite3.connect('database.db')
		cursor = sqliteConnection.cursor()
		print("Database created and Successfully Connected to SQLite")
		cursor.execute(query)
		sqliteConnection.commit()
		cursor.close()

	except sqlite3.Error as error:
		print("Error while connecting to sqlite", error)
	finally:
		if sqliteConnection:
			sqliteConnection.close()

def execute_query(query, alter):
	try:
		sqliteConnection = sqlite3.connect('database.db')
		cursor = sqliteConnection.cursor()
		cursor.execute(query)
		if alter : sqliteConnection.commit()
		result = cursor.fetchall()
		print(result)
		return result
		#cursor.close()

	except sqlite3.Error as error:
		print("Error while connecting to sqlite", error)
	finally:
		if sqliteConnection:
			sqliteConnection.close()



def get_tetris_record1(user_name):
	query = "SELECT record1 FROM users WHERE username="+user_name
	return execute_query(query)

def get_tetris_record2(user_name):
	query = "SELECT record2 FROM users WHERE username="+user_name
	return execute_query(query)

def get_tetris_record3(user_name):
	query = "SELECT record3 FROM users WHERE username="+user_name
	return execute_query(query)

def get_tetris_record4(user_name):
	query = "SELECT record4 FROM users WHERE username="+user_name
	return execute_query(query)

def get_tetris_record5(user_name):
	query = "SELECT record5 FROM users WHERE username="+user_name
	return execute_query(query)

def get_user_password(user_name):
	query = "SELECT password FROM users WHERE username="+user_name
	return execute_query(query)

def get_user_name(user_name_introduced):
	query = "SELECT * FROM users WHERE username="+"'"+user_name_introduced+"'"
	return execute_query(query, False)

def update_tetris_records(score, record_index):
	query = "UPDATE users SET record"+str(record_index)+"="+str(score)
	return execute_query(query)

def add_user(user_name, password):
	values = "('"+user_name+"', '"+password+"')"
	query = "INSERT INTO users(username, password) VALUES"+values
	return execute_query(query, True)

