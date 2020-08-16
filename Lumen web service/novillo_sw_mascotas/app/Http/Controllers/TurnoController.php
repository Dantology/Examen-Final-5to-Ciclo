<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Turno;
use Illuminate\Support\Facades\DB;

class TurnoController extends Controller
{
    public function __construct()
    {
        //
    }
    function all(Request $request)
    {
        if ($request->isJson()) {
            //Eloquent
            $turnos = Turno::all();
            return response()->json($turnos, 200);
        }
        return response()->json(['error' => 'Unauthorized'], 401, []);
    }
    public function solicitar(Request $request){
        if ($request->isJson()) {
            $data = $request->json()->all();
            $clientes=DB::select("SELECT * FROM modelo_cliente WHERE cedula = '". $data['cedula'] ."';");
            $id_cliente=$clientes[0]->cliente_id;
            $mascotas=DB::select("SELECT * FROM modelo_mascota WHERE cliente_id = '". $id_cliente ."';");
            $id_mascota=$mascotas[0]->mascota_id;
            if($id_cliente){
                $turno=Turno::create([
                    "mascota_id"=>$id_mascota, 
                    "descripcion"=>$data['descripcion'],
                    "responsable"=>$data['responsable'],
                    "fecha"=>$data['fecha'],
               ]);
            }
            return response()->json($turno, 200);
        }
        return response()->json(['error' => 'Unauthorized'], 401, []);
    }

    
}
