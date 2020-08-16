<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Str;
use Illuminate\Database\Eloquent\ModelNotFoundException;
use App\User;
use Illuminate\Support\Facades\Auth;

class UserController extends Controller
{
    public function __construct()
    {
        //
    }

    function index()
    {
        //Eloquent
        $user = Auth::user();
        return response()->json($user, 200);
    }

    //
    public function all(Request $request)
    {
        if ($request->isJson()) {
            $users = User::all();
            return response()->json($users, 200);
        }
    }

    public function login(Request $request)
    {
        if ($request->isJson()) {
            try {
                $data = $request->json()->all();
                $user = User::where('username', $data['username'])->first();
                if ($this->django_password_verify($data['password'], $user->password)) {
                    $info = "Bienvenido";
                    $user->api_token = Str::random(60);
                    $user->save();
                    return response()->json($user, 200);
                } else {
                    return response()->json(['error' => 'Usuario o contrasenia invalidas'], 406);
                }
            } catch (ModelNotFoundException $e) {
                return response()->json(['error' => 'Unauthorized'], 406);
            }
        }
    }


    function django_password_verify(string $password, string $djangoHash)
    {
        $pieces = explode('$', $djangoHash);
        if (count($pieces) !== 4) {
            throw new Exception("Illegal hash format");
        }
        list($header, $iter, $salt, $hash) = $pieces;
        // Get the hash algorithm used:
        if (preg_match('#^pbkdf2_([a-z0-9A-Z]+)$#', $header, $m)) {
            $algo = $m[1];
        } else {
            throw new Exception(sprintf("Bad header (%s)", $header));
        }
        if (!in_array($algo, hash_algos())) {
            throw new Exception(sprintf("Illegal hash algorithm (%s)", $algo));
        }

        $calc = hash_pbkdf2(
            $algo,
            $password,
            $salt,
            (int) $iter,
            32,
            true
        );
        return hash_equals($calc, base64_decode($hash));
    }
}
