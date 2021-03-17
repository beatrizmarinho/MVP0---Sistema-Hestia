import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private HttpClient: HttpClient) { }

  public getClientes(){
    return this.HttpClient.get('http://127.0.0.1:5000/api/cliente');

  }

  public postClientes(cliente:any){
    return this.HttpClient.post('http://127.0.0.1:5000/api/cliente', cliente);

  }

  public getImoveis(){
    return this.HttpClient.get('http://127.0.0.1:5000/api/imovel');
  
  }

  public postImoveis(imovel:any){
    return this.HttpClient.post('http://127.0.0.1:5000/api/imovel', imovel);

  }
  public getCompras(){
    return this.HttpClient.get('http://127.0.0.1:5000/api/compra');
  
  }

  public postCompras(compra:any){
    return this.HttpClient.post('http://127.0.0.1:5000/api/compra', compra);

  }

  public getProprietarios(){
    return this.HttpClient.get('http://127.0.0.1:5000/api/proprietario');

  }

  public postProprietarios(proprietario:any){
    return this.HttpClient.post('http://127.0.0.1:5000/api/proprietario', proprietario);

  }

  public getGastos(){
    return this.HttpClient.get('http://127.0.0.1:5000/api/gastos');
  
  }

  public postGastos(gasto:any){
    return this.HttpClient.post('http://127.0.0.1:5000/api/gastos', gasto);

  }

  
}