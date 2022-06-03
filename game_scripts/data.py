import pymysql

connection = pymysql.connect(
	host = 'localhost',
	user = 'root',
	password = '',
	db = 'arcade_machine'
)

cursor = connection.cursor()

def get_tetris_record1(user_name):
	query = "SELECT record1 FROM users WHERE user_name="+user_name
	cursor.execute(query)
	connection.commit()

def get_tetris_record2(user_name):
	query = "SELECT record2 FROM users WHERE user_name="+user_name
	cursor.execute(query)
	connection.commit()

def get_tetris_record3(user_name):
	query = "SELECT record3 FROM users WHERE user_name="+user_name
	cursor.execute(query)
	connection.commit()

def get_tetris_record4(user_name):
	query = "SELECT record4 FROM users WHERE user_name="+user_name
	cursor.execute(query)
	connection.commit()

def get_tetris_record5(user_name):
	query = "SELECT record5 FROM users WHERE user_name="+user_name
	cursor.execute(query)
	connection.commit()


def get_user_password(user_name):
	query = "SELECT password FROM users WHERE user_name="+user_name
	cursor.execute(query)
	connection.commit()

def get_user_name(user_name_introduced):
	query = "SELECT * FROM users WHERE user_name="+user_name_introduced
	cursor.execute(query)
	connection.commit()

def update_tetris_records(score, record_index):
	query = "UPDATE users SET record"+str(record_index)+"="+str(score)
	cursor.execute(query)
	connection.commit()

def add_user(user_name, password):
	values = '('+user_name+','+password+')'
	query = "INSERT INTO users(user_name, password) VALUES"+values
	cursor.execute(query)
	connection.commit()

