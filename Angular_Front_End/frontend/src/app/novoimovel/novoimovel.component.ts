import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service'

@Component({
  selector: 'app-novoimovel',
  templateUrl: './novoimovel.component.html',
  styleUrls: ['./novoimovel.component.scss']
})
export class NovoimovelComponent implements OnInit {

    constructor(private ApiService: ApiService) { }

  ngOnInit(): void {  
  }

  inputNovoImovel(tipo:string, logradouro:string, numero:string, complemento:string, cep:string, bairro:string, cidade:string, uf:string, id_proprietario:string, data_posse: string ){
      this.ApiService.postImoveis({ "tipo":tipo, "logradouro":logradouro, "numero":numero, "complemento":complemento, "cep":cep, "bairro":bairro, "cidade":cidade, "uf":uf, "id_proprietario":id_proprietario, "data_posse":data_posse }).subscribe(data => {
        console.log(data)
      },
      error  => {
      console.log("Error", error);
      });
  }
}
