import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ClienteComponent } from './cliente/cliente.component';
import { ImovelComponent } from './imovel/imovel.component';
import { NovoclienteComponent } from './novocliente/novocliente.component';
import { MenuComponent} from './menu/menu.component';
import { NovoimovelComponent } from './novoimovel/novoimovel.component';
import { CompraComponent } from './compra/compra.component';
import { NovacompraComponent } from './novacompra/novacompra.component';
import { ProprietarioComponent } from './proprietario/proprietario.component';
import { NovoproprietarioComponent } from './novoproprietario/novoproprietario.component';
import { GastosComponent } from './gastos/gastos.component';
import { NovosgastosComponent } from './novosgastos/novosgastos.component';

const routes: Routes = [
  {path: 'cliente', component: ClienteComponent},
  {path: 'imovel', component: ImovelComponent},
  {path:'novocliente', component: NovoclienteComponent},
  {path:'menu', component: MenuComponent},
  {path:'', pathMatch: 'full', redirectTo: '/menu'},
  {path:'novoimovel', component: NovoimovelComponent},
  {path:'compra', component: CompraComponent},
  {path:'novacompra', component: NovacompraComponent},
  {path:'proprietario', component: ProprietarioComponent},
  {path:'novoproprietario', component: NovoproprietarioComponent},
  {path:'gastos', component: GastosComponent},
  {path:'novosgastos', component: NovosgastosComponent},


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
