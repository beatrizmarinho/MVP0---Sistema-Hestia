from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource, fields, abort
from flask_cors import CORS



flask_app = Flask(__name__)
flask_app.config.from_object("config")
app = Api(app = flask_app, 
		version = "1.0", 
		title = "Hestia", 
		description = "Sistema de Compra e Venda de Imóveis")

CORS(flask_app)
name_space = app.namespace('api', description='Dados de compra e venda de Imóveis')

db = SQLAlchemy(flask_app)
