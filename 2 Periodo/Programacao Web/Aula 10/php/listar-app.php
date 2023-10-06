<?php
    $con = mysqli_connect("localhost:3306", "root", "PUC@1234", "pucpr");

    $query = mysqli_query($con, "SELECT * FROM aplicativo");

    $dados = array();

    while($resultado = mysqli_fetch_assoc($query)) {
        array_push($dados, $resultado);
    }

    $dados_json = json_encode($dados);
    echo $dados_json;

?>