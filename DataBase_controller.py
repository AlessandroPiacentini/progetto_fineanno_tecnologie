import sqlite3

class Database:
    _instance = None
    _conn = None

    @staticmethod
    def getInstance():
        if Database._instance is None:
            Database._instance = Database()
        return Database._instance

    def __init__(self):
        self._conn = sqlite3.connect('gestione_spese.db')

    def updateTable(self, table, fields, where=None):
        sql = f"UPDATE {table} SET "
        sql += ', '.join([f"{field} = ?" for field in fields.keys()])
        params = list(fields.values())
        if where is not None:
            sql += " WHERE " + ' AND '.join([f"{field} = ?" for field in where.keys()])
            params.extend(list(where.values()))
        self._execute(sql, params)

    def execute_query(self, sql):
        cur = self._conn.cursor()
        cur.execute(sql)
        self._conn.commit()

    def read_table(self, table, where=None):
        sql = f"SELECT * FROM {table}"
        params = []
        if where is not None:
            sql += " WHERE " + ' AND '.join([f"{field} = ?" for field in where.keys()])
            params = list(where.values())
        return self._execute(sql, params)

    def delete(self, table, where):
        sql = f"DELETE FROM {table} WHERE " + ' AND '.join([f"{field} = ?" for field in where.keys()])
        params = list(where.values())
        self._execute(sql, params)

    def insert(self, table, fields):
        sql = f"INSERT INTO {table} (" + ', '.join(fields.keys()) + ") VALUES (" + ', '.join(['?']*len(fields)) + ")"
        params = list(fields.values())
        self._execute(sql, params)

    def _execute(self, sql, params):
        cur = self._conn.cursor()
        cur.execute(sql, params)
        self._conn.commit()
        return cur.fetchall()
