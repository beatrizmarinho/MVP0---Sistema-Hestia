from flask_restplus import Api, Resource, fields, abort
from sistema_hestia.hestia.api import app, db, name_space
from flask import Flask, request, jsonify
from sistema_hestia.hestia.api.models import Compra


model_1 = app.model('Creating Compra', 
				  {
                      "id_cliente": fields.String(required = True, 
    					  				 description="ID do cliente", 
    					  				 help="ID não pode estar em branco."),
                      "id_imovel": fields.String(required = True, 
    					  				 description="ID do imovel", 
    					  				 help="ID não pode estar em branco."),
					  "data_compra": fields.String(required = True, 
    					  				 description="Data da compra", 
    					  				 help="Data da compra não pode estar em branco."),
					  "valor_imovel": fields.String(required = True, 
    					  				 description="Valor do imovel", 
    					  				 help="Valor do imovel não pode estar em branco."),
					  "financiamento": fields.String(required = True, 
    					  				 description="Financiamento", 
    					  				 help="Financiamento não pode estar em branco."),
					  "porcent_entrada": fields.String(required = True, 
    					  				 description="Porcentagem de entrada"), 
					  "qtd_parcelas": fields.String(required = True, 
    					  				 description="Quantidade de parcelas do financiamento"), 
					  "banco_financiador": fields.String(required = True, 
    					  				 description="Banco financiador do cliente")
              }
)

@name_space.route("/compra")
class CompraAPI(Resource):
	@app.doc(responses={ 200: 'OK', 500: 'Internal Error' })
	def get(self):
		compras = Compra.query.all()
		lista_compras = []

		for compra in compras:
			compra_atual = {}
			compra_atual['id_compra']=compra.id_compra
			compra_atual['id_cliente']=compra.id_cliente
			compra_atual['id_imovel']=compra.id_imovel
			compra_atual['data_compra']=compra.data_compra
			compra_atual['valor_imovel']=compra.valor_imovel
			compra_atual['financiamento']=compra.financiamento
			compra_atual['porcent_entrada']=compra.porcent_entrada
			compra_atual['qtd_parcelas']=compra.qtd_parcelas
			compra_atual['banco_financiador']=compra.banco_financiador
			lista_compras.append(compra_atual)
		return jsonify(lista_compras)

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Internal Error' })
	@app.expect(model_1)		
	def post(self):
		try:
			payload = request.get_json()
			compra = Compra(id_cliente=payload["id_cliente"], id_imovel=payload["id_imovel"], data_compra=payload["data_compra"], 
						  	valor_imovel=payload["valor_imovel"], financiamento=payload["financiamento"], 
						  	porcent_entrada=payload["porcent_entrada"], qtd_parcelas=payload["qtd_parcelas"], 
						  	banco_financiador=payload["banco_financiador"])
		
		except TypeError:
			abort(400)
		try:
			db.session.add(compra)
			db.session.commit()
		except:
			abort(500)
		return jsonify(payload)		
		