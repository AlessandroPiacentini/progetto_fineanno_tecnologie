import mysql.connector

class Database:
    _instance = None
    _conn = None

    def __init__(self):
        if not Database._instance:
            Database._instance = self
            self._dbname = "gestione_spese"
            self._conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database=self._dbname
            )
        else:
            raise Exception("Non puoi creare un'altra istanza di questa classe.")

    @staticmethod
    def getInstance():
        if not Database._instance:
            Database()
        return Database._instance

    def updateTable(self, table, fields, where=None):
        sql = f"UPDATE {table} SET "
        params = []
        for field, value in fields.items():
            sql += f"{field} = %s, "
            params.append(value)
        sql = sql.rstrip(', ')
        if where is not None:
            sql += " WHERE "
            for field, value in where.items():
                sql += f"{field} = %s AND "
                params.append(value)
            sql = sql.rstrip(" AND ")
        cur = self._conn.cursor()
        cur.execute(sql, params)
        self._conn.commit()

    def execute_query(self, sql):
        cur = self._conn.cursor()
        cur.execute(sql)
        self._conn.commit()
        return cur.fetchall()

    def read_table(self, table, where=None):
        sql = f"SELECT * FROM {table}"
        params = None
        if where is not None:
            sql += " WHERE "
            params = []
            for field, value in where.items():
                sql += f"{field} = %s AND "
                params.append(value)
            sql = sql.rstrip(" AND ")
        cur = self._conn.cursor()
        if params is not None:
            cur.execute(sql, params)
        else:
            cur.execute(sql)
        return cur.fetchall()

    def delete(self, table, where):
        sql = f"DELETE FROM {table} WHERE "
        params = []
        for field, value in where.items():
            sql += f"{field} = %s AND "
            params.append(value)
        sql = sql.rstrip(" AND ")
        cur = self._conn.cursor()
        cur.execute(sql, params)
        self._conn.commit()

    def insert(self, table, data):
        sql = f"INSERT INTO {table} ("
        values = " VALUES ("
        params = []
        for field, value in data.items():
            sql += f"{field}, "
            values += "%s, "
            params.append(value)
        sql = sql.rstrip(', ') + ")"
        values = values.rstrip(', ') + ")"
        sql += values
        cur = self._conn.cursor()
        cur.execute(sql, params)
        self._conn.commit()
