import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-novosgastos',
  templateUrl: './novosgastos.component.html',
  styleUrls: ['./novosgastos.component.scss']
})
export class NovosgastosComponent implements OnInit {

  constructor(private ApiService: ApiService) { }

  ngOnInit(): void {  
  }

  inputNovosGastos(id_imovel:string, conta_luz:string, conta_agua:string, condominio:string, propaganda_venda:string ){
      this.ApiService.postGastos({ "id_imovel": id_imovel, "conta_luz":conta_luz, "conta_agua":conta_agua, "condominio":condominio, "propaganda_venda":propaganda_venda }).subscribe(data => {
        console.log(data)
      },
      error  => {
      console.log("Error", error);
      });


  }

}