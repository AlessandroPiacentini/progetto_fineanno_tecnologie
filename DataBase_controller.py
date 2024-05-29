import sqlite3
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
        self._db_file = 'gestione_spese.db'

    def _create_connection(self):
        try:
            conn = sqlite3.connect(self._db_file)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite: {e}")
            return None

    def check_user(self, username, password):
        sql = "SELECT * FROM users WHERE username=? AND password=?"
        params = (username, password)
        return self._execute_fetchall(sql, params)

    def inserisci_user(self, username, password):
        sql = "INSERT INTO users (username, password) VALUES (?, ?)"
        params = (username, password)
        self._execute_commit(sql, params)
        
    def delete_spesa(self, id):
        sql = "DELETE FROM spese WHERE id=?"
        params = (id,)
        self._execute_commit(sql, params)
        
    def get_spese_from_id_user(self, id_user):
        sql = "SELECT * FROM spese WHERE id_user=?"
        params = (id_user,)
        return self._execute_fetchall(sql, params)
    
    def get_spese_from_id_user_this_month(self, id_user):
        sql = "SELECT * FROM spese WHERE id_user=? AND strftime('%m', data)=strftime('%m', 'now')"
        params = (id_user,)
        return self._execute_fetchall(sql, params)
    
    def get_spese_from_id_user_this_year(self, id_user):
        sql = "SELECT * FROM spese WHERE id_user=? AND strftime('%Y', data)=strftime('%Y', 'now')"
        params = (id_user,)
        return self._execute_fetchall(sql, params)
    
    def get_spese_from_id_user_this_week(self, id_user):
        sql = "SELECT * FROM spese WHERE id_user=? AND strftime('%W', data)=strftime('%W', 'now')"
        params = (id_user,)
        return self._execute_fetchall(sql, params)
    
    def get_spese_from_id_user_from_date(self, id_user, month, year):
        sql = "SELECT * FROM spese WHERE id_user=? AND strftime('%m', data)=? AND strftime('%Y', data)=?"
        params = (id_user, month, year)
        return self._execute_fetchall(sql, params)
    
    def insert_spesa(self, titolo, dettagli, prezzo, data, id_user):
        sql = "INSERT INTO spese (titolo, dettagli, prezzo, data, id_user) VALUES (?, ?, ?, ?, ?)"
        params = (titolo, dettagli, prezzo, data, id_user)
        self._execute_commit(sql, params)

    def _execute_commit(self, sql, params):
        conn = self._create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, params)
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error executing query: {e}")
                conn.rollback()
            finally:
                conn.close()

    def _execute_fetchall(self, sql, params):
        conn = self._create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, params)
                return cursor.fetchall()
            except sqlite3.Error as e:
                print(f"Error executing query: {e}")
                return []
            finally:
                conn.close()
        else:
            return []

