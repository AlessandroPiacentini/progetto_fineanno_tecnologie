import mysql.connector
from mysql.connector import Error
import threading

class Database:
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def getInstance():
        if Database._instance is None:
            with Database._lock:
                if Database._instance is None:
                    Database._instance = Database()
        return Database._instance

    def __init__(self):
        self._config = {
            'host': "localhost",
            'user': "root",
            'password': "",
            'database': "gestione_spese"
        }

    def _create_connection(self):
        try:
            conn = mysql.connector.connect(**self._config)
            return conn
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def check_user(self, username, password):
        sql = "SELECT * FROM users WHERE username=%s AND password=%s"
        params = (username, password)
        return self._execute_fetchall(sql, params)

    def inserisci_user(self, username, password):
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        params = (username, password)
        self._execute_commit(sql, params)
        
    def delete_spesa(self, id):
        sql = "DELETE FROM spese WHERE id=%s"
        params = (id,)
        self._execute_commit(sql, params)
        
    def get_spese_from_id_user(self, id_user):
        sql = "SELECT * FROM spese WHERE id_user=%s"
        params = (id_user,)
        return self._execute_fetchall(sql, params)
    
    def get_spese_from_id_user_this_month(self, id_user):
        sql = "SELECT * FROM spese WHERE id_user=%s AND MONTH(data)=MONTH(CURDATE())"
        params = (id_user,)
        return self._execute_fetchall(sql, params)
    
    def get_spese_from_id_user_this_year(self, id_user):
        sql = "SELECT * FROM spese WHERE id_user=%s AND YEAR(data)=YEAR(CURDATE())"
        params = (id_user,)
        return self._execute_fetchall(sql, params)
    
    def get_spese_from_id_user_this_week(self, id_user):
        sql = "SELECT * FROM spese WHERE id_user=%s AND WEEK(data)=WEEK(CURDATE())"
        params = (id_user,)
        return self._execute_fetchall(sql, params)
    
    def get_spese_from_id_user_from_month(self, id_user, month):
        sql = "SELECT * FROM spese WHERE id_user=%s AND MONTH(data)=%s"
        params = (id_user, month)
        return self._execute_fetchall(sql, params)
    
    def insert_spesa(self, titolo, dettagli, prezzo, data, id_user):
        sql = "INSERT INTO spese (titolo, dettagli, prezzo, data, id_user) VALUES (%s, %s, %s, %s, %s)"
        params = (titolo, dettagli, prezzo, data, id_user)
        self._execute_commit(sql, params)

    def _execute_commit(self, sql, params):
        conn = self._create_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql, params)
                    conn.commit()
            except Error as e:
                print(f"Error executing query: {e}")
                conn.rollback()
            finally:
                conn.close()

    def _execute_fetchall(self, sql, params):
        conn = self._create_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql, params)
                    return cursor.fetchall()
            except Error as e:
                print(f"Error executing query: {e}")
                return []
            finally:
                conn.close()
        else:
            return []
