import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-compra',
  templateUrl: './compra.component.html',
  styleUrls: ['./compra.component.scss']
})

export class CompraComponent implements OnInit {
  compras:any;
  constructor(private ApiService: ApiService) { }

  ngOnInit(): void {
    this.mostrarCompra();
  }

  mostrarCompra(){
    this.ApiService.getCompras().subscribe((data)=>{console.log(data);this.compras=data});
  }

}