from sistema_hestia.hestia.api import db

class Gastos(db.Model):
	__tablename__ = "gastos"
	id_gastos = db.Column('id_gastos', db.Integer, primary_key = True, autoincrement = True, unique = True)
	id_imovel = db.Column(db.Integer, db.ForeignKey('imovel.id_imovel'))
	conta_luz = db.Column(db.String(55))
	conta_agua = db.Column(db.String(55))
	condominio = db.Column(db.String(55))
	propaganda_venda = db.Column(db.String(55))

	def __init__(self, id_imovel, conta_luz, conta_agua, condominio, propaganda_venda):
		self.id_imovel = id_imovel
		self.conta_luz = conta_luz
		self.conta_agua = conta_agua
		self.condominio = condominio
		self.propaganda_venda = propaganda_venda
