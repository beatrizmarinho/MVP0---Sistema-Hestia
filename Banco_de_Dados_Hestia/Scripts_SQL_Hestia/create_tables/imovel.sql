create table public.imovel (id_imovel serial PRIMARY KEY NOT NULL, 
							 tipo varchar(200) NOT NULL, 
							 logradouro varchar(255)NOT NULL,
							 numero varchar(5)NOT NULL,
							 complemento varchar(30),
							 CEP char(8) NOT NULL,
							 bairro varchar(55),
							 cidade varchar (55),
							 UF char(2));