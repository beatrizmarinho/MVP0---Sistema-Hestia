import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service'


@Component({
  selector: 'app-cliente',
  templateUrl: './cliente.component.html',
  styleUrls: ['./cliente.component.scss']
})
export class ClienteComponent implements OnInit {
  clientes:any;
  constructor(private ApiService: ApiService) { }

  ngOnInit(): void {
    this.mostrarCliente();
   }


  mostrarCliente(){
    this.ApiService.getClientes().subscribe((data)=>{console.log(data);this.clientes=data});
  }


}


