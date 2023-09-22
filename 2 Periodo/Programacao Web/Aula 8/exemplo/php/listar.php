<?php
    $con = mysqli_connect("localhost:3306", "root", "PUC@1234", "pucpr");
    $resultado = mysqli_query($con, "SELECT * FROM estudante");
    $dados = array();

    while ($registro = mysqli_fetch_assoc($resultado)) {
        array_push($dados, $registro);
    }

    $json_dados = json_encode($dados);
    echo $json_dados;
?>