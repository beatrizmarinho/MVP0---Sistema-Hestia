create table public.imovel_proprietario (id_imovel_proprietario serial PRIMARY KEY NOT NULL,
	                                     id_proprietario int NOT NULL,
                                         FOREIGN KEY (id_proprietario) REFERENCES public.proprietario (id_proprietario),
										 id_imovel int NOT NULL,
                                         FOREIGN KEY (id_imovel) REFERENCES public.imovel (id_imovel),
                                         data_posse date NOT NULL);
