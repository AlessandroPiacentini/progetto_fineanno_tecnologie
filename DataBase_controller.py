import mysql.connector

class Database:
    _instance = None

    def __init__(self):
        if not Database._instance:
            Database._instance = self
            self._dbname = "gestione_spese"
            try:
                self._conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database=self._dbname
                )
            except mysql.connector.Error as err:
                print(f"Errore di connessione al database: {err}")
                raise

        else:
            raise Exception("Non puoi creare un'altra istanza di questa classe.")

    @staticmethod
    def getInstance():
        if not Database._instance:
            Database()
        return Database._instance

    def updateTable(self, table, fields, where=None):
        try:
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
        except mysql.connector.Error as err:
            print(f"Errore durante l'aggiornamento della tabella: {err}")
            raise

    def execute_query(self, sql):
        try:
            cur = self._conn.cursor()
            cur.execute(sql)
            self._conn.commit()
            return cur.fetchall()
        except mysql.connector.Error as err:
            print(f"Errore durante l'esecuzione della query: {err}")
            raise
        finally:
            cur.close()

    def read_table(self, table, where=None):
        try:
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
            self._conn.commit()
            return cur.fetchall()
        except mysql.connector.Error as err:
            print(f"Errore durante la lettura della tabella: {err}")
            raise
        finally:
            cur.close()

    def delete(self, table, where):
        try:
            sql = f"DELETE FROM {table} WHERE "
            params = []
            for field, value in where.items():
                sql += f"{field} = %s AND "
                params.append(value)
            sql = sql.rstrip(" AND ")
            cur = self._conn.cursor()
            cur.execute(sql, params)
            self._conn.commit()
        except mysql.connector.Error as err:
            print(f"Errore durante l'eliminazione dei dati: {err}")
            raise
        finally:
            cur.close()

    def insert(self, table, data):
        try:
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
        except mysql.connector.Error as err:
            print(f"Errore durante l'inserimento dei dati: {err}")
            raise
        finally:
            cur.close()
