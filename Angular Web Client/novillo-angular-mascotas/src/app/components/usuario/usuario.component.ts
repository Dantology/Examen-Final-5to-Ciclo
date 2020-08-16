import { Component } from '@angular/core';
import {UsuarioService} from './../../services/usuario.service';
@Component({
  selector: 'app-usuario',
  templateUrl: './usuario.component.html',
  styleUrls: ['./usuario.component.css']
})
export class UsuarioComponent {

  constructor(private usuario_servicio: UsuarioService) { }

  getUsers() {
    this.usuario_servicio.getUsers().subscribe(datos =>{
      console.log(datos);
    });
  }

}
