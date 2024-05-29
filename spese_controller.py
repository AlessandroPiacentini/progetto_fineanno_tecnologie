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
        
        @self.app.route('/elimina', methods=['GET'])
        def elimina():
            id = request.args.get('id', type=int)
            return self.delete_spesa(id)
            
        @self.app.route('/get_spese_settimana')
        def get_spese_settimana():
            return self.retrieve_spese_settimana(session['id'])
        
        @self.app.route('/get_spese_anno')
        def get_spese_anno():
            return self.retrieve_spese_anno(session['id'])
        
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
        
        self.db.insert_spesa(titolo, dettagli, prezzo, data, session['id'])   
        
        
        
    def retrieve_spese_settimana(self, id_user):
        result=self.db.get_spese_from_id_user_this_week(id_user)
        return jsonify(result)
    
    
    def retrieve_spese_anno(self, id_user):
        result=self.db.get_spese_from_id_user_this_year(id_user)
        return jsonify(result)

            
        
    
    def delete_spesa(self, id):
        if id is None:
                return jsonify({"error": "ID non valido"}), 400
            
        try:
            self.db.delete_spesa(id)
            return jsonify(True)
        except Exception as e:
            return jsonify({"error": str(e)}), 500  
                
    def retrieve_spese(self):
        result = self.db.get_spese_from_id_user(session['id'])
        return jsonify(result)
    
    def retrieve_spese_mese(self):
        where = {"id_user": session['id']}
        result = self.db.get_spese_from_id_user_this_month(session['id'])
        return jsonify(result)
