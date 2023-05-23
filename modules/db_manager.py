import sqlite3

from sqlite3 import Error
from enum import IntEnum

database = "../database/aiven.db"


class Mode(IntEnum):
    DATING = 1
    FRIENDLY = 2


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


# NOTE: Parameters are dictionaries
def create_user(username, pw):
    conn = create_connection(database)
    user = [username, pw]
    with conn:
        try:
            sql = "INSERT INTO user (username, pw) VALUES (?,?)"
            cur = conn.cursor()
            cur.execute(sql, user)
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)


def create_like(user_like, username, conn):
    like = [user_like, username]
    try:
        sql = "INSERT INTO u_like (user_like, user_id) VALUES (?,?)"
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute(sql, like)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)


def create_dislike(user_dislike, username, conn):
    dislike = [user_dislike, username]
    try:
        sql = "INSERT INTO u_dislike (user_dislike, user_id) VALUES (?,?)"
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        cur.execute(sql, dislike)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)


def edit_user_profile(u_username, u_gender, u_bio, likes, dislikes):
    conn = create_connection(database)
    create_like(likes, u_username, conn)
    create_dislike(dislikes, u_username, conn)

    profile = [u_gender, u_bio, u_username]
    with conn:
        try:
            sql = "UPDATE user SET gender=?, bio=? WHERE username=?"
            cur = conn.cursor()
            cur.execute(sql, profile)
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)


# Create a new chat
def create_chat(mode, title, username):
    conn = create_connection(database)
    chat = [mode, title, username]
    with conn:
        try:
            sql = "INSERT INTO chat (mode, title, username) VALUES (?,?,?)"
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute(sql, chat)
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)


def create_msg(content, sender, date_sent, time_sent, chat_id):
    conn = create_connection(database)
    msg = [content, sender, date_sent, time_sent, chat_id]
    with conn:
        try:
            sql = "INSERT INTO message (content, sender, date_sent, time_sent, chat_id) VALUES (?,?,?,?,?)"
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute(sql, msg)
            conn.commit()
            return cur.lastrowid
        except Error as e:
            print(e)


# Return all messages in that chat
def select_msg_by_chat(chat_id):
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM message WHERE chat_id = ?", (chat_id,))
        rows = cur.fetchall()
        return rows


# Get likes of the user
def select_likes(user_id):
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM u_like WHERE user_id = ?", (user_id,))
        rows = cur.fetchall()
        return rows


# Get dislikes of the user
def select_dislikes(user_id):
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM u_dislike WHERE user_id = ?", (user_id,))
        rows = cur.fetchall()
        return rows


def select_chats_by_user(username):
    conn = create_connection(database)
    with conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM chat WHERE user_id = ?", (username,))
            rows = cur.fetchall()
            return rows
        except Error as e:
            print(e)


# Get the user
def select_user(username, value="*"):
    conn = create_connection(database)
    with conn:
        try:
            cur = conn.cursor()
            cur.execute(f"SELECT {value} FROM user WHERE username = ?", (username,))
            rows = cur.fetchall()
            return rows
        except Error as e:
            print(e)

