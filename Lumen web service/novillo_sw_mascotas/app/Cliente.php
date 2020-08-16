<?php
namespace App;
use Illuminate\Database\Eloquent\Model;

class Cliente extends Model{
    protected $table = 'modelo_cliente';
    protected $fillable = ['cedula','nombres','apellidos','email','celular',];
    public $timestamps=false;
    protected $hidden=['cliente_id',];
}
