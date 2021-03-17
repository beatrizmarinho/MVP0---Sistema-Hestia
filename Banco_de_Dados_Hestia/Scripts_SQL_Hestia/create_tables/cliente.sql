create table public.cliente (id_cliente serial PRIMARY KEY NOT NULL, 
							 nome varchar(255) NOT NULL, 
							 CPF char(11) NOT NULL, 
							 RG char(9) NOT NULL,
							 data_nasc date NOT NULL, 
							 estado_civil varchar(10) NOT NULL,
							 profissao varchar(35) NOT NULL,
							 logradouro varchar(255)NOT NULL,
							 numero varchar(5)NOT NULL,
							 complemento varchar(30),
							 CEP char(8) NOT NULL,
							 bairro varchar(55),
							 cidade varchar (55),
							 UF char(2));










