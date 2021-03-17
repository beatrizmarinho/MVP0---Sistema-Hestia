import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service'


@Component({
  selector: 'app-imovel',
  templateUrl: './imovel.component.html',
  styleUrls: ['./imovel.component.scss']
})
export class ImovelComponent implements OnInit {
  imoveis:any;
  constructor(private ApiService: ApiService) { }

  ngOnInit(): void {
    this.mostrarImovel();
  }

  mostrarImovel(){
    this.ApiService.getImoveis().subscribe((data)=>{console.log(data);this.imoveis=data});
  }

}