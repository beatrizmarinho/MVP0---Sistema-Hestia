create table public.compra (id_compra serial PRIMARY KEY NOT NULL, 
							id_cliente int NOT NULL,
							  FOREIGN KEY (id_cliente) REFERENCES public.cliente (id_cliente),
							  id_imovel int NOT NULL,
							  FOREIGN KEY (id_imovel) REFERENCES public.imovel (id_imovel),
							data_compra date NOT NULL, 
							valor_imovel varchar(50) NOT NULL,
							financiamento boolean NOT NULL,
							porcent_entrada varchar(50),
							qtd_parcelas varchar(10),
							banco_financiador varchar(55));