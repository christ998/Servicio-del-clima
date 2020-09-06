<?php
    $bd = new SQLite3('db.sqlite3');

    $res = $bd->query("SELECT ciudad from modelo_ciudades");
    $res = $res->fetchArray();
    $res = json_encode($res);
    echo $res;
?>