import sqlite3

# Crea una connessione al database
conn = sqlite3.connect('gestione_spese.db')

# Crea un cursore
c = conn.cursor()

# Crea la tabella 'users'
c.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
""")

# Crea la tabella 'spese'
c.execute("""
    CREATE TABLE spese (
        id INTEGER PRIMARY KEY,
        id_user INTEGER,
        titolo TEXT NOT NULL,
        dettagli TEXT,
        prezzo REAL,
        img_path TEXT,
        data TEXT,
        FOREIGN KEY(id_user) REFERENCES users(id)
    )
""")

# Esegui il commit delle modifiche
conn.commit()

# Chiudi la connessione
conn.close()
