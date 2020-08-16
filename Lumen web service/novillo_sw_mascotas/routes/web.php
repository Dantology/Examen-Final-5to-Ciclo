<?php

/** @var \Laravel\Lumen\Routing\Router $router */

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

$router->get('/', function () use ($router) {
    return $router->app->version();
});

$router->group(['prefix'=>'usuarios'], function($router){
    $router->get('all', 'UserController@all');
    $router->post('ingresar','UserController@login');
});


$router->group(['middleware' => ['auth']], function () use ($router) {
    $router->group(['prefix'=>'cliente'], function($router){
        $router->get('',['uses' => 'ClienteController@all']);
        $router->post('create','ClienteController@createCliente');
       
    });

    $router->group(['prefix'=>'mascotas'], function($router){
        $router->get('',['uses'=>'MascotasController@all']);
        $router->get('{cedula}',['uses' => 'ClienteController@getMascotas']);
        $router->post('create',['uses' => 'MascotasController@createMascota']);
    });

    $router->group(['prefix'=>'turnos'], function($router){
        $router->get('',['uses'=>'TurnoController@all']);
        $router->post('solicitar',['uses' => 'TurnoController@solicitar']);
    });
});