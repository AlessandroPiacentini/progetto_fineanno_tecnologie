import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('gestione_spese.db')
        cursor = conn.cursor()

        # Creazione della tabella `users`
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # Creazione della tabella `spese`
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS spese (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_user INTEGER,
                titolo TEXT NOT NULL,
                dettagli TEXT,
                prezzo REAL,
                data DATE,
                FOREIGN KEY (id_user) REFERENCES users(id)
            )
        ''')

        conn.commit()
        print("Database created successfully.")

    except sqlite3.Error as e:
        print(f"Error creating database: {e}")
    finally:
        conn.close()

def insert_data():
    try:
        conn = sqlite3.connect('gestione_spese.db')
        cursor = conn.cursor()

        # Inserimento dei dati nella tabella `users`
        cursor.execute('''
            INSERT INTO users (id, username, password)
            VALUES (1, 'Piace', '189bbbb00c5f1fb7fba9ad9285f193d1')
        ''')

        # Inserimento dei dati nella tabella `spese`
        cursor.executemany('''
            INSERT INTO spese (id, id_user, titolo, dettagli, prezzo, data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', [
            (12, 1, 'titolo12', 'dettagli12', 120, '2024-01-12'),
            (13, 1, 'titolo13', 'dettagli13', 130, '2024-01-13'),
            (14, 1, 'titolo14', 'dettagli14', 140, '2024-01-14'),
            (15, 1, 'titolo15', 'dettagli15', 500, '2024-01-15'),
            (16, 1, 'titolo16', 'dettagli16', 160, '2024-05-16'),
            (17, 1, 'titolo17', 'dettagli17', 170, '2024-05-17'),
            (18, 1, 'titolo18', 'dettagli18', 180, '2024-01-18'),
            (19, 1, 'titolo19', 'dettagli19', 190, '2024-01-19'),
            (20, 1, 'titolo20', 'dettagli20', 200, '2024-01-20'),
            (23, 1, 'prova spesa di oggi', 'lanncnacnacacnac', 20, '2024-05-29'),
            (24, 1, 'prova spesa ieri', 'AXABOANXAIOCAJCKJABCABC', 800, '2024-05-28'),
            (25, 1, 'spesa del 1900', 'lnxpaonacancancao ni ', 500, '1997-06-04'),
            (26, 1, 'prodotto con decimale', 'papxjoajjacaojcpa', 10.5, '2024-05-04')
        ])

        conn.commit()
        print("Data inserted successfully.")

    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_database()
    insert_data()
