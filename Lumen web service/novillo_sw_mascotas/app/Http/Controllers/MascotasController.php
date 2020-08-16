<?php

namespace App\Http\Controllers;

use App\Mascota;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class MascotasController extends Controller
{
    function all(Request $request)
    {
        if ($request->isJson()) {
            //Eloquent
            $mascotas = Mascota::all();
            return response()->json($mascotas, 200);
        }
        return response()->json(['error' => 'Unauthorized'], 401, []);
    }

    function createMascota(Request $request)
    {
        if ($request->isJson()) {
            $data = $request->json()->all();
            $clientes = DB::select("SELECT * FROM modelo_cliente WHERE cedula = '" . $data['cedula'] . "';");
            $id_cliente = $clientes[0]->cliente_id;
            if ($id_cliente) {
                $mascota = Mascota::create([
                    "cliente_id" => $id_cliente,
                    "nombre" => $data['nombre'],
                    "raza" => $data['raza'],
                    "altura" => $data['altura'],
                    "tipo" => $data['tipo'],
                ]);
            }
            return response()->json($mascota, 200);
        }
        return response()->json(['error' => 'Unauthorized'], 401, []);
    }
}
