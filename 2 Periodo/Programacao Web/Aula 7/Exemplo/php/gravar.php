<?php
    $nome = $_POST["nome"];
    $email = $_POST["email"];
    $senha = $_POST["senha"];

    $conexao = mysqli_connect("localhost:3306", "root", "PUC@1234", "pucpr");

    $query = "INSERT INTO estudante (nome, email, senha) VALUES('$nome', '$email', '$senha')";

    mysqli_query($conexao, $query);

?>