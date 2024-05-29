## Descrizione

E' una web app sviluppata con Python e Flask per aiutarti a gestire le tue spese personali in modo semplice ed efficiente. Con questa applicazione, puoi tenere traccia delle tue uscite.

## Funzionalità

- **Autenticazione Utente**: Registrazione e login per garantire la sicurezza dei dati.
- **Gestione Spese**: Aggiungi ed elimina le spese.
- **Report e Grafici**: Visualizza grafici delle tue spese.

## Tecnologie Utilizzate

- **Backend**: Python, Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Grafici**: Chart.js

## Installazione

### Prerequisiti

- Python 3
- Pip (Python package installer)

### Passi per l'installazione

1. Clona il repository
    ```bash
    git clone https://github.com/tuo-username/expense-manager.git
    cd expense-manager
    ```


3. Installa le dipendenze
    ```bash
    pip install -r requirements.txt
    ```

4. Inizializza il database
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Esegui l'applicazione
    ```bash
    flask run
    ```

L'app sarà disponibile su `http://127.0.0.1:5000`.

