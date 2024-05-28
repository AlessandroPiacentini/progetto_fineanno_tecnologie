import sqlite3

# Connessione al database SQLite
conn = sqlite3.connect('gestione_spese.db')
c = conn.cursor()

# Creazione della tabella 'users'
c.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Inserimento dei dati nella tabella 'users'
c.execute("INSERT INTO users (id, username, password) VALUES (?, ?, ?)", (1, 'Piace', '189bbbb00c5f1fb7fba9ad9285f193d1'))

# Creazione della tabella 'spese'
c.execute('''
    CREATE TABLE spese (
        id INTEGER PRIMARY KEY,
        id_user INTEGER,
        titolo TEXT NOT NULL,
        dettagli TEXT,
        prezzo REAL,
        data TEXT,
        FOREIGN KEY(id_user) REFERENCES users(id)
    )
''')

# Inserimento dei dati nella tabella 'spese'
spese_data = [
    (8, 1, 'titolo8', 'dettagli8', 80, '2024-01-08'),
    (9, 1, 'titolo9', 'dettagli9', 90, '2024-01-09'),
    (10, 1, 'titolo10', 'dettagli10', 100, '2024-01-10'),
    (11, 1, 'titolo11', 'dettagli11', 110, '2024-01-11'),
    (12, 1, 'titolo12', 'dettagli12', 120, '2024-01-12'),
    (13, 1, 'titolo13', 'dettagli13', 130, '2024-01-13'),
    (14, 1, 'titolo14', 'dettagli14', 140, '2024-01-14'),
    (15, 1, 'titolo15', 'dettagli15', 150, '2024-01-15'),
    (16, 1, 'titolo16', 'dettagli16', 160, '2024-05-16'),
    (17, 1, 'titolo17', 'dettagli17', 170, '2024-05-17'),
    (18, 1, 'titolo18', 'dettagli18', 180, '2024-01-18'),
    (19, 1, 'titolo19', 'dettagli19', 190, '2024-01-19'),
    (20, 1, 'titolo20', 'dettagli20', 200, '2024-01-20')
]

c.executemany("INSERT INTO spese (id, id_user, titolo, dettagli, prezzo, data) VALUES (?, ?, ?, ?, ?, ?)", spese_data)

# Commit delle modifiche e chiusura della connessione
conn.commit()
conn.close()
