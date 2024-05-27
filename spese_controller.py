import os
from flask import Flask, redirect, request, jsonify, session
from werkzeug.utils import secure_filename
from DataBase_controller import Database

class SpeseController:
    db = None
    def __init__(self, app):
        self.db = Database.getInstance()  # Inizializza l'istanza del database
        self.app = app
        self.register_routes()
        
    def register_routes(self):
        @self.app.route('/get_spese')
        def get_spese():
            return self.retrieve_spese()
        
        
        @self.app.route('/get_spese_mese')
        def get_spese_mese():
            return self.retrieve_spese_mese()
        
        @self.app.route('/add_spesa', methods=['POST'])
        def add_spesa():
            titolo = request.form.get('titolo')
            descrizione = request.form.get('descrizione')
            prezzo = request.form.get('prezzo')
            data = request.form.get('data')
            
            self.add_spesa_to_db(titolo, descrizione, prezzo, data)  

            return redirect('/spese')
                
    def add_spesa_to_db(self, titolo, dettagli, prezzo, data):
        data = {
            "id_user": session['id'],
            "titolo": titolo,
            "dettagli": dettagli,
            "prezzo": prezzo,
            "data": data
        }
        self.db.insert('spese', data)     
                
    def retrieve_spese(self):
        where = {"id_user": session['id']}
        result = self.db.read_table('spese', where=where)
        return jsonify(result)
    
    def retrieve_spese_mese(self):
        where = {"id_user": session['id']}
        result = self.db.execute_query('SELECT * FROM spese WHERE month(data) = month(now())')
        return jsonify(result)
