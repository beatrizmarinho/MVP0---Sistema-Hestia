INSERT INTO public.cliente(
	id_cliente, nome, cpf, rg, data_nasc, estado_civil, profissao, logradouro, numero, complemento, cep, bairro, cidade, uf)
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);