from flask_restplus import Api, Resource, fields, abort
from sistema_hestia.hestia.api import app, db, name_space
from flask import Flask, request, jsonify
from sistema_hestia.hestia.api.models import Gastos

model_4 = app.model('Creating Gastos', 
				  {
                      "id_imovel": fields.String(required = True, 
    					  				 description="ID do imovel", 
    					  				 help="ID não pode estar em branco."),
					  "conta_luz": fields.String(required = True, 
    					  				 description="Conta de luz", 
    					  				 help="Conta de luz não pode estar em branco."),
					  "conta_agua": fields.String(required = True, 
    					  				 description="Conta de agua", 
    					  				 help="Conta de agua não pode estar em branco."),
					  "condominio": fields.String(required = True, 
    					  				 description="Condominio", 
    					  				 help="Condominio não pode estar em branco."),
					  "propaganda_venda": fields.String(required = True, 
    					  				 description="Propaganda de venda do imovel",
										 help="Propaganda não pode estar em branco."),
              }
)

@name_space.route("/gastos")
class GastosAPI(Resource):
	@app.doc(responses={ 200: 'OK', 500: 'Internal Error' })
	def get(self):
		gastos = Gastos.query.all()
		lista_gastos = []

		for gasto in gastos:
			gastos_atual = {}
			gastos_atual['id_gastos']=gasto.id_gastos
			gastos_atual['id_imovel']=gasto.id_imovel
			gastos_atual['conta_luz']=gasto.conta_luz
			gastos_atual['conta_agua']=gasto.conta_agua
			gastos_atual['condominio']=gasto.condominio
			gastos_atual['propaganda_venda']=gasto.propaganda_venda
			lista_gastos.append(gastos_atual)
		return jsonify(lista_gastos)
	

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Internal Error' })
	@app.expect(model_4)		
	def post(self):
		try:
			payload = request.get_json()
			gastos = Gastos(id_imovel=payload["id_imovel"], conta_luz=payload["conta_luz"], 
						  	conta_agua=payload["conta_agua"], condominio=payload["condominio"], 
						  	propaganda_venda=payload["propaganda_venda"])
		
		except TypeError:
			abort(400)
		try:
			db.session.add(gastos)
			db.session.commit()
		except:
			abort(500)
		return jsonify(payload)
