import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-novacompra',
  templateUrl: './novacompra.component.html',
  styleUrls: ['./novacompra.component.scss']
})
export class NovacompraComponent implements OnInit {

  constructor(private ApiService: ApiService) { }

  ngOnInit(): void {  
  }

  inputNovaCompra(id_cliente:string, id_imovel:string, data_compra:string, valor_imovel:string, financiamento:boolean, porcent_entrada:string, qtd_parcelas:string, banco_financiador:string ){
      this.ApiService.postCompras({ "id_cliente":id_cliente, "id_imovel": id_imovel, "data_compra":data_compra, "valor_imovel":valor_imovel, "financiamento":financiamento, "porcent_entrada":porcent_entrada, "qtd_parcelas":qtd_parcelas, "banco_financiador":banco_financiador}).subscribe(data => {
        console.log(data)
      },
      error  => {
      console.log("Error", error);
      });


  }

}