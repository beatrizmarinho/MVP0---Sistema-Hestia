from sistema_hestia.hestia.api import db

class Proprietario(db.Model):
	__tablename__ = "proprietario"
	id_proprietario = db.Column('id_proprietario', db.Integer, primary_key = True, autoincrement = True, unique = True)
	nome = db.Column(db.String(255))
	cpf = db.Column(db.String(11))
	rg = db.Column(db.String(9)) 
	data_nasc = db.Column(db.String(10))
	estado_civil = db.Column(db.String(10))
	profissao = db.Column(db.String(10))

	def __init__(self, nome, cpf, rg, data_nasc, estado_civil, profissao):
		self.nome = nome
		self.cpf = cpf
		self.rg = rg
		self.data_nasc = data_nasc
		self.estado_civil = estado_civil
		self.profissao = profissao
