from sistema_hestia.hestia.api import db

class Imovel_proprietario(db.Model):
	__tablename__ = "imovel_proprietario"
	id_imovel_proprietario = db.Column('id_imovel_proprietario', db.Integer, primary_key = True, autoincrement = True, unique = True)
	id_proprietario = db.Column(db.Integer, db.ForeignKey('proprietario.id_proprietario'))
	id_imovel = db.Column(db.Integer, db.ForeignKey('imovel.id_imovel'))
	data_posse = db.Column(db.DateTime)
	


	def __init__(self, id_proprietario, id_imovel, data_posse):
		self.id_proprietario = id_proprietario
		self.id_imovel = id_imovel
		self.data_posse = data_posse
