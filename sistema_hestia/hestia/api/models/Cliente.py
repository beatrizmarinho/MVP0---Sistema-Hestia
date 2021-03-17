from sistema_hestia.hestia.api import db

class Cliente(db.Model):
	__tablename__ = "cliente"
	id_cliente = db.Column('id_cliente', db.Integer, primary_key = True, autoincrement = True, unique = True)
	nome = db.Column(db.String(255))
	cpf = db.Column(db.String(11))
	rg = db.Column(db.String(9)) 
	data_nasc = db.Column(db.String(10))
	estado_civil = db.Column(db.String(10))
	profissao = db.Column(db.String(10))
	logradouro = db.Column(db.String(255))
	numero = db.Column(db.String(5))
	complemento = db.Column(db.String(30))
	cep = db.Column(db.String(8))
	bairro = db.Column(db.String(55))
	cidade = db.Column(db.String(55))
	uf = db.Column(db.String(2))

	def __init__(self, nome, cpf, rg, data_nasc, estado_civil, profissao, logradouro, numero, complemento, cep, bairro, cidade, uf):
		self.nome = nome
		self.cpf = cpf
		self.rg = rg
		self.data_nasc = data_nasc
		self.estado_civil = estado_civil
		self.profissao = profissao
		self.logradouro = logradouro
		self.numero = numero
		self.complemento = complemento
		self.cep = cep
		self.bairro = bairro
		self.cidade = cidade
		self.uf = uf
