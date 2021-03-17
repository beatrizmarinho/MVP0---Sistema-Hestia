import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service'


@Component({
  selector: 'app-novocliente',
  templateUrl: './novocliente.component.html',
  styleUrls: ['./novocliente.component.scss']
})
export class NovoclienteComponent implements OnInit {
 
  constructor(private ApiService: ApiService) { }

  ngOnInit(): void {  
  }

  inputNovoCliente(nome:string, cpf:string, rg:string, data_nasc:string, estado_civil:string, profissao:string, logradouro:string, numero:string, complemento:string, cep:string, bairro:string, cidade:string, uf:string ){
      this.ApiService.postClientes({ "nome":nome, "cpf": cpf, "rg":rg, "data_nasc":data_nasc, "estado_civil":estado_civil, "profissao":profissao, "logradouro":logradouro, "numero":numero, "complemento":complemento, "cep":cep, "bairro":bairro, "cidade":cidade, "uf":uf }).subscribe(data => {
        console.log(data)
      },
      error  => {
      console.log("Error", error);
      });
  }

}
