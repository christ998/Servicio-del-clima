<?php

class Ciudad {
    public $name;
    public $id;
}

$xml = simplexml_load_file("list-CL.xml");
$ciudades = array();
foreach ($xml->loc as $nodo) 
	{
	    $aux = new Ciudad();
        $aux->name=$nodo->name;
        $aux->id = $nodo->id;
        
        array_push($ciudades,$aux);
	}

$bd = new SQLite3('db.db');
foreach($ciudades as $dato){
$bd->exec("INSERT INTO modelo_ciudades ('ciudad','ident') VALUES ('".$dato->name."', ".intval($dato->id).")");
}

$bd->exec("select * from modelo_ciudades");


?>
