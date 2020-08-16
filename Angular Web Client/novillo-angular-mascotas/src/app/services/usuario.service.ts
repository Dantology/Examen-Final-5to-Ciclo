import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Usuario } from './../interfaces/usuario';
@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private http: HttpClient) { }

  getUsers() {
    const path = "http://localhost:8000/usuarios/all";
    return this.http.get<Usuario[]>(path,{
      headers: {'Content-Type':'application/json'}
    });
  }

}

