<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Cliente;
use Illuminate\Support\Facades\DB;

class ClienteController extends Controller
{
    public function __construct()
    {
        //
    }

    //
    public function all(Request $request){
        $clientes = Cliente::all();
        return response()->json($clientes,200);
    }


    public function getClienteCedula(Request $request, $cedula){
        if($request->isJson()){
            $cliente = Cliente::where('cedula',$cedula)->get();
            if(!$cliente->isEmpty()){
                return response()->json($cliente,200);
            }else {
                return response()->json(['error'=>'No existe el cliente'],401,[]);
            }
        }
        return response()->json(['error'=>'Unauthorized'],401,[]);
    }

    public function getMascotas(Request $request, $cedula){
        if($request->isJson()){
            $mascotas= DB::select("select * from modelo_mascota where cliente_id = (select cliente_id from modelo_cliente where cedula = ". $cedula .");");
            
            return response()->json($mascotas,200);
        }
        return response()->json(['error'=>'Unauthorized'],401,[]);
    }

    public function createCliente(Request $request){
        if($request->isJson()){
            $data = $request->json()->all();
            $cliente = Cliente::create([
                'cedula' => $data['cedula'],
                'nombres' => $data['nombres'],
                'apellidos' => $data['apellidos'],
                "email" => $data['email'],
                "celular" => $data['celular'],
            ]);
            return response()->json($data,200);
        }
        return response()->json(['error'=>'Unauthorized'],401,[]);
    }
/*
    public function depositar(Request $request){
        if($request->json()){
            $cuenta = Cuenta::where('numero', $request->numero)->get();

        }
    }
*/
    
}
