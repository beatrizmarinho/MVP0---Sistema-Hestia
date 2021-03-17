import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ClienteComponent } from './cliente/cliente.component';
import { ImovelComponent } from './imovel/imovel.component';
import { NovoclienteComponent } from './novocliente/novocliente.component';
import { MenuComponent } from './menu/menu.component';
import { NovoimovelComponent } from './novoimovel/novoimovel.component';
import { CompraComponent } from './compra/compra.component';
import { NovacompraComponent } from './novacompra/novacompra.component';
import { ProprietarioComponent } from './proprietario/proprietario.component';
import { NovoproprietarioComponent } from './novoproprietario/novoproprietario.component';
import { GastosComponent } from './gastos/gastos.component';
import { NovosgastosComponent } from './novosgastos/novosgastos.component';

@NgModule({
  declarations: [
    AppComponent,
    ClienteComponent,
    ImovelComponent,
    NovoclienteComponent,
    MenuComponent,
    NovoimovelComponent,
    CompraComponent,
    NovacompraComponent,
    ProprietarioComponent,
    NovoproprietarioComponent,
    GastosComponent,
    NovosgastosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
