import { Component} from '@angular/core';
import {ClienteService} from './../../services/cliente.service';
import {Cliente} from './../../interfaces/cliente';

@Component({
  selector: 'app-cliente',
  templateUrl: './cliente.component.html',
  styleUrls: ['./cliente.component.css']
})
export class ClienteComponent {

  constructor(private cliente_servicio: ClienteService) { }

  getAllCliente(){
    this.cliente_servicio.getAllCliente().subscribe(datos=>{
      console.log(datos);
    });
  }

}
