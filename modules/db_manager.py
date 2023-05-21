import sqlite3
from sqlite3 import Error

database = "../database/aiven.db"

def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return conn


def create_user(user):
	conn = create_connection(database)
	with conn:
		sql = "INSERT INTO user (username, pw, d_name, bio, age) VALUES (?,?,?,?,?)"
		cur = conn.cursor()
		cur.execute(sql, user)
		conn.commit()
		return cur.lastrowid


def create_chat(chat):
	conn = create_connection(database)
	with conn:
		sql = "INSERT INTO chat (id, mode, title, date_modified, date_created) VALUES (?,?,?,?,?)"
		cur = conn.cursor()
		cur.execute(sql, chat)
		conn.commit()
		return cur.lastrowid


def create_msg(msg):
	conn = create_connection(database)
	with conn:
		sql = "INSERT INTO message (id, content, sender, date_sent, time_sent, chat_id) VALUES (?,?,?,?,?,?)"
		cur = conn.cursor()
		cur.execute(sql, msg)
		conn.commit()
		return cur.lastrowid


def select_msg_by_chat(chat_id):
	conn = create_connection(database)
	with conn:
		cur = conn.cursor()
	    cur.execute("SELECT * FROM message WHERE chat_id = ?", (chat_id,))
	    rows = cur.fetchall()
	    return rows


def select_likes(user_id):
	conn = create_connection(database)
	with conn:
		cur = conn.cursor()
	    cur.execute("SELECT * FROM u_like WHERE user_id = ?", (user_id,))
	    rows = cur.fetchall()
	    return rows


def select_dislikes(user_id):
	conn = create_connection(database)
	with conn:
		cur = conn.cursor()
	    cur.execute("SELECT * FROM u_dislike WHERE user_id = ?", (user_id,))
	    rows = cur.fetchall()
	    return rows


def select_user(username):
	conn = create_connection(database)
	with conn:
		cur = conn.cursor()
	    cur.execute("SELECT * FROM user WHERE username = ?", (username,))
	    rows = cur.fetchall()
	    return rows

