from flask_restplus import Api, Resource, fields, abort
from sistema_hestia.hestia.api import app, db, name_space
from flask import Flask, request, jsonify
from sistema_hestia.hestia.api.models import Cliente


#criar modelo de dados de post de cliente
model = app.model('Creating Cliente', 
				  {
                      "nome": fields.String(required = True, 
    					  				 description="Nome do cliente", 
    					  				 help="Nome não pode estar em branco."),
                      "cpf": fields.String(required = True, 
    					  				 description="CPF do cliente", 
    					  				 help="CPF não pode estar em branco."),
					  "rg": fields.String(required = True, 
    					  				 description="RG do cliente", 
    					  				 help="RG não pode estar em branco."),
					  "data_nasc": fields.String(required = True, 
    					  				 description="Data de nascimento do cliente", 
    					  				 help="Data de nascimento não pode estar em branco."),
					  "estado_civil": fields.String(required = True, 
    					  				 description="Estado civil do cliente", 
    					  				 help="Estado civil do cliente não pode estar em branco."),
					  "profissao": fields.String(required = True, 
    					  				 description="Profissao do cliente", 
    					  				 help="Profissao não pode estar em branco."),
					  "logradouro": fields.String(required = True, 
    					  				 description="Logradouro do cliente", 
    					  				 help="Logradouro não pode estar em branco."),
					  "numero": fields.String(required = True, 
    					  				 description="Numero do logradouro do cliente", 
    					  				 help="Numero não pode estar em branco."),
					  "complemento": fields.String(required = True, 
    					  				 description="Complemento do logradouro do cliente"),
    				  "cep": fields.String(required = True, 
    					  				 description="CEP do cliente", 
    					  				 help="CEP não pode estar em branco."),
				       "bairro": fields.String(required = True, 
    					  				 description="Bairro do cliente", 
    					  				 help="Bairro não pode estar em branco."),	
					   "cidade": fields.String(required = True, 
    					  				 description="Cidade do cliente", 
    					  				 help="Cidade não pode estar em branco."),		
					    "uf": fields.String(required = True, 
    					  				 description="UF do cliente", 
    					  				 help="UF não pode estar em branco."),
              }
)

@name_space.route("/cliente")
class ClienteAPI(Resource):
	@app.doc(responses={ 200: 'OK', 500: 'Internal Error' })
	def get(self):
		clientes = Cliente.query.all()
		lista_clientes = []

		for cliente in clientes:
			cliente_atual = {}
			cliente_atual['id_cliente']=cliente.id_cliente
			cliente_atual['nome']=cliente.nome
			cliente_atual['cpf']=cliente.cpf
			cliente_atual['rg']=cliente.rg
			cliente_atual['data_nasc']=cliente.data_nasc
			cliente_atual['estado_civil']=cliente.estado_civil
			cliente_atual['profissao']=cliente.profissao
			cliente_atual['logradouro']=cliente.logradouro
			cliente_atual['numero']=cliente.numero
			cliente_atual['complemento']=cliente.complemento
			cliente_atual['cep']=cliente.cep
			cliente_atual['bairro']=cliente.bairro
			cliente_atual['cidade']=cliente.cidade
			cliente_atual['uf']=cliente.uf
			lista_clientes.append(cliente_atual)
		return jsonify(lista_clientes)

	@app.expect(model)
	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Internal Error' })
	def post(self):
		try:
			payload = request.get_json()
			cliente = Cliente(nome=payload["nome"], cpf=payload["cpf"], rg=payload["rg"], 
							data_nasc=payload["data_nasc"], estado_civil=payload["estado_civil"], 
							profissao=payload["profissao"], logradouro=payload["logradouro"], 
							numero=payload["numero"], complemento=payload["complemento"], 
							cep=payload["cep"], bairro=payload["bairro"], cidade=payload["cidade"], 
							uf=payload["uf"])
		except TypeError:
			abort(400)
		try:
			db.session.add(cliente)
			db.session.commit()
		except:
			abort(500)
		return jsonify(payload)    
		