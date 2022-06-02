from pygame import Cursor
import pymysql

connection = pymysql.connect(
	host = 'localhost',
	user = 'root',
	password = '',
	db = 'arcade_machine'
)

cursor = connection.cursor()

def update_tetris_records(score):
	connection.commit()

def add_user(user_name, password):
	connection.commit()
