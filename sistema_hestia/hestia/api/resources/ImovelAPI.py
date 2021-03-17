from flask_restplus import Api, Resource, fields, abort
from sistema_hestia.hestia.api import app, db, name_space
from flask import Flask, request, jsonify
from sistema_hestia.hestia.api.models import Imovel, Imovel_proprietario
from sqlalchemy import inspect


model_2 = app.model('Creating Imovel', 
				  {
                      "tipo": fields.String(required = True, 
    					  				 description="Tipo de imovel", 
    					  				 help="Tipo não pode estar em branco."),
					  "logradouro": fields.String(required = True, 
    					  				 description="Logradouro do imovel", 
    					  				 help="Logradouro não pode estar em branco."),
					  "numero": fields.String(required = True, 
    					  				 description="Numero do logradouro do imovel", 
    					  				 help="Numero não pode estar em branco."),
					  "complemento": fields.String(required = True, 
    					  				 description="Complemento do logradouro do imovel"),
    				  "cep": fields.String(required = True, 
    					  				 description="CEP do imovel", 
    					  				 help="CEP não pode estar em branco."),
				       "bairro": fields.String(required = True, 
    					  				 description="Bairro do imovel", 
    					  				 help="Bairro não pode estar em branco."),	
					   "cidade": fields.String(required = True, 
    					  				 description="Cidade do imovel", 
    					  				 help="Cidade não pode estar em branco."),		
					    "uf": fields.String(required = True, 
    					  				 description="UF do imovel", 
    					  				 help="UF não pode estar em branco."),
						 "data_posse": fields.String(required = True, 
    					   				 description="Data da posse imovel", 
    					   				 help="Data não pode estar em branco."),
						 "id_proprietario": fields.String(required = True, 
    					   				 description="ID do proprietario", 
    					   				 help="ID não pode estar em branco.")

              }
)

@name_space.route("/imovel")
class ImovelAPI(Resource):
	@app.doc(responses={ 200: 'OK', 500: 'Internal Error' })
	def get(self):
		imoveis = Imovel.query\
			.join(Imovel_proprietario, Imovel.id_imovel == Imovel_proprietario.id_imovel)\
			.add_columns(
				Imovel.id_imovel,
				Imovel.tipo,
				Imovel.logradouro,
				Imovel.numero,
				Imovel.complemento,
				Imovel.cep,
				Imovel.bairro, 
				Imovel.cidade,
				Imovel.uf,
				Imovel_proprietario.data_posse, Imovel_proprietario.id_proprietario)\
			.all()
			
		lista_imoveis = []
		for imovel in imoveis:
			imovel_atual = {}
			imovel_atual['id_imovel']=imovel.id_imovel
			imovel_atual['tipo']=imovel.tipo
			imovel_atual['logradouro']=imovel.logradouro
			imovel_atual['numero']=imovel.numero
			imovel_atual['complemento']=imovel.complemento
			imovel_atual['cep']=imovel.cep
			imovel_atual['bairro']=imovel.bairro
			imovel_atual['cidade']=imovel.cidade
			imovel_atual['uf']=imovel.uf
			imovel_atual['data_posse']=imovel.data_posse
			imovel_atual['id_proprietario']=imovel.id_proprietario
			lista_imoveis.append(imovel_atual)
		return jsonify(lista_imoveis)

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Internal Error' })
	@app.expect(model_2)		
	def post(self):
		try:
			payload = request.get_json()
			imovel = Imovel(tipo=payload["tipo"], logradouro=payload["logradouro"], 
						  	numero=payload["numero"], complemento=payload["complemento"], 
						  	cep=payload["cep"], bairro=payload["bairro"], cidade=payload["cidade"], 
						  	uf=payload["uf"])
		except TypeError:
			abort(400)
		try:
			db.session.add(imovel)
			db.session.commit()
			imovel_pk = inspect(imovel).identity[0]
			imovel_proprietario = Imovel_proprietario(data_posse=payload["data_posse"], id_proprietario=payload["id_proprietario"], id_imovel=imovel_pk)
			db.session.add(imovel_proprietario)
			db.session.commit()
		except:
			abort(500)
		return jsonify(payload)
