import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Cliente} from './../interfaces/cliente';

@Injectable({
  providedIn: 'root'
})
export class ClienteService {

  private host="http://localhost:8000/cliente";
  constructor(private http: HttpClient) { }

  getAllCliente(){
    const path=`${this.host}/all`;
    return this.http.get<Cliente[]>(path,{
      headers:{'Content-Type':'application/json','api_token':"Qz90hY5aqyM9aGQCHzsYUVznyzP6Mjrup8mXgF24e8TclVJIDxny9QXhZx4c"
    }
    });


  }
}
