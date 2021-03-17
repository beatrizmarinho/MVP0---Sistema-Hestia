import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service'

@Component({
  selector: 'app-novoproprietario',
  templateUrl: './novoproprietario.component.html',
  styleUrls: ['./novoproprietario.component.scss']
})
export class NovoproprietarioComponent implements OnInit {

  constructor(private ApiService: ApiService) { }

  ngOnInit(): void {  
  }

  inputNovoProprietario(nome:string, cpf:string, rg:string, data_nasc:string, estado_civil:string, profissao:string){
      this.ApiService.postProprietarios({ "nome":nome, "cpf": cpf, "rg":rg, "data_nasc":data_nasc, "estado_civil":estado_civil, "profissao":profissao}).subscribe(data => {
        console.log(data)
      },
      error  => {
      console.log("Error", error);
      });
  }
}
