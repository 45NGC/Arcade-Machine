import pymysql

connection = pymysql.connect(
	host = 'localhost',
	user = 'root',
	password = '',
	db = 'arcade_machine'
)

cursor = connection.cursor()

def get_tetris_record1():
	query = "SELECT record1 FROM tetris_records"
	cursor.execute(query)
	connection.commit()

def get_tetris_record2():
	query = "SELECT record2 FROM tetris_records"
	cursor.execute(query)
	connection.commit()

def get_tetris_record3():
	query = "SELECT record3 FROM tetris_records"
	cursor.execute(query)
	connection.commit()

def get_tetris_record4():
	query = "SELECT record4 FROM tetris_records"
	cursor.execute(query)
	connection.commit()

def get_tetris_record5():
	query = "SELECT record5 FROM tetris_records"
	cursor.execute(query)
	connection.commit()

def update_tetris_records(score, record_index):
	query = "UPDATE tetris_records SET record"+str(record_index)+"="+str(score)
	cursor.execute(query)
	connection.commit()

def add_user(user_name, password):
	values = '('+user_name+','+password+')'
	query = "INSERT INTO users(name, password) VALUES"+values
	connection.commit()
