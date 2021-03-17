create table public.proprietario (id_proprietario serial PRIMARY KEY NOT NULL, 
							      nome varchar(255) NOT NULL, 
							      CPF char(11) NOT NULL, 
							      RG char(9) NOT NULL,
							      data_nasc date NOT NULL, 
							      estado_civil varchar(10) NOT NULL,
							      profissao varchar(35) NOT NULL);