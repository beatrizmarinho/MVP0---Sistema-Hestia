from sistema_hestia.hestia.api import db

class Imovel(db.Model):
	__tablename__ = "imovel"
	id_imovel = db.Column('id_imovel', db.Integer, primary_key = True, autoincrement = True, unique = True)
	tipo = db.Column(db.String(200))
	logradouro = db.Column(db.String(255))
	numero = db.Column(db.String(5))
	complemento = db.Column(db.String(30))
	cep = db.Column(db.String(8))
	bairro = db.Column(db.String(55))
	cidade = db.Column(db.String(55))
	uf = db.Column(db.String(2))

	def __init__(self, tipo, logradouro, numero, complemento, cep, bairro, cidade, uf):
		self.tipo = tipo
		self.logradouro = logradouro
		self.numero = numero
		self.complemento = complemento
		self.cep = cep
		self.bairro = bairro
		self.cidade = cidade
		self.uf = uf
