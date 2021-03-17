INSERT INTO public.compra(
	id_compra, id_cliente, id_imovel, data_compra, valor_imovel, financiamento, porcent_entrada, qtd_parcelas, banco_financiador)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);