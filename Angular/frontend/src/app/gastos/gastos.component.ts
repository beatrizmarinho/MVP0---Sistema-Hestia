import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-gastos',
  templateUrl: './gastos.component.html',
  styleUrls: ['./gastos.component.scss']
})
export class GastosComponent implements OnInit {
    gastos:any;
  constructor(private ApiService: ApiService) { }

  ngOnInit(): void {
    this.mostrarGastos();
  }

  mostrarGastos(){
    this.ApiService.getGastos().subscribe((data)=>{console.log(data);this.gastos=data});
  }

}