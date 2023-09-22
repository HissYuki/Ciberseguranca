<?php
    $conn = mysqli_connect("localhost:3306", "root", "PUC@1234", "pucpr");
    $resultado = mysqli_query($conn, "SELECT * FROM musica");
    $dados = array();

    while ($registro = mysqli_fetch_assoc($resultado)) {
        array_push($dados, $registro);
    }

    $dados_json = json_encode($dados);
    echo $dados_json;

?>