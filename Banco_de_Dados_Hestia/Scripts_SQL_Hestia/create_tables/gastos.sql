create table public.gastos (id_gastos serial PRIMARY KEY NOT NULL, 
							  id_imovel int NOT NULL,
							  FOREIGN KEY (id_imovel) REFERENCES public.imovel (id_imovel),
			                  conta_luz varchar(55),
							  conta_agua varchar(55),
							  condominio varchar(55),
							  propaganda_venda varchar(55));