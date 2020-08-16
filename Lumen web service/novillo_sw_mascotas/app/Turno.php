<?php
namespace App;
use Illuminate\Database\Eloquent\Model;

class Turno extends Model{
    protected $table = 'modelo_turno';
    protected $primaryKey = 'turno_id';
    protected $fillable = ['fecha','descripcion','responsable','mascota_id',];
    public $timestamps=false;
    protected $hidden=['turno_id',];
}
