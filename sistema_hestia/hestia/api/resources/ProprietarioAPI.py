from flask_restplus import Api, Resource, fields, abort
from sistema_hestia.hestia.api import app, db, name_space
from flask import Flask, request, jsonify
from sistema_hestia.hestia.api.models import Proprietario


model_3 = app.model('Creating Proprietario', 
				  {
                      "nome": fields.String(required = True, 
    					  				 description="Nome do proprietario", 
    					  				 help="Nome não pode estar em branco."),
                      "cpf": fields.String(required = True, 
    					  				 description="CPF do proprietario", 
    					  				 help="CPF não pode estar em branco."),
					  "rg": fields.String(required = True, 
    					  				 description="RG do proprietario", 
    					  				 help="RG não pode estar em branco."),
					  "data_nasc": fields.String(required = True, 
    					  				 description="Data de nascimento do proprietario", 
    					  				 help="Data de nascimento não pode estar em branco."),
					  "estado_civil": fields.String(required = True, 
    					  				 description="Estado civil do proprietario", 
    					  				 help="Estado civil do proprietario não pode estar em branco."),
					  "profissao": fields.String(required = True, 
    					  				 description="Profissao do proprietario", 
    					  				 help="Profissao não pode estar em branco.")
              }
)

@name_space.route("/proprietario")
class ProprietarioAPI(Resource):
	@app.doc(responses={ 200: 'OK', 500: 'Internal Error' })
	def get(self):
		proprietarios = Proprietario.query.all()
		lista_proprietarios = []

		for proprietario in proprietarios:
			proprietario_atual = {}
			proprietario_atual['id_proprietario']=proprietario.id_proprietario
			proprietario_atual['nome']=proprietario.nome
			proprietario_atual['cpf']=proprietario.cpf
			proprietario_atual['rg']=proprietario.rg
			proprietario_atual['data_nasc']=proprietario.data_nasc
			proprietario_atual['estado_civil']=proprietario.estado_civil
			proprietario_atual['profissao']=proprietario.profissao
			lista_proprietarios.append(proprietario_atual)
		return jsonify(lista_proprietarios)

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Internal Error' })
	@app.expect(model_3)		
	def post(self):
		try:
			payload = request.get_json()
			proprietario = Proprietario(nome=payload["nome"], cpf=payload["cpf"], rg=payload["rg"], 
						  				data_nasc=payload["data_nasc"], estado_civil=payload["estado_civil"], 
						  				profissao=payload["profissao"])
		
		except TypeError:
			abort(400)
		try:
		db.session.add(proprietario)
		db.session.commit()
		except:
			abort(500)
		return jsonify(payload)
		