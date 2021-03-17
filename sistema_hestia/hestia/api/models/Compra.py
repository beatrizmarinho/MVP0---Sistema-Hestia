from sistema_hestia.hestia.api import db

class Compra(db.Model):
	__tablename__ = "compra"
	id_compra = db.Column('id_compra', db.Integer, primary_key = True, autoincrement = True, unique = True)
	id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'))
	id_imovel = db.Column(db.Integer, db.ForeignKey('imovel.id_imovel'))
	data_compra = db.Column(db.DateTime)
	valor_imovel = db.Column(db.String(35))
	financiamento = db.Column(db.Boolean)
	porcent_entrada = db.Column(db.String(10))
	qtd_parcelas = db.Column(db.String(3))
	banco_financiador = db.Column(db.String(20))

	def __init__(self, id_cliente, id_imovel, data_compra, valor_imovel, financiamento, porcent_entrada, qtd_parcelas, banco_financiador):
		self.id_cliente = id_cliente
		self.id_imovel = id_imovel
		self.data_compra = data_compra
		self.valor_imovel = valor_imovel
		self.financiamento = financiamento
		self.porcent_entrada = porcent_entrada
		self.qtd_parcelas = qtd_parcelas
		self.banco_financiador = banco_financiador
