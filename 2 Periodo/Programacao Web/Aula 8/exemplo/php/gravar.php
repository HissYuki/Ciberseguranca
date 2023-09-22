<?php
    $con = mysqli_connect("localhost:3306", "root", "PUC@1234", "pucpr");

    $nome = $_POST["nome"];
    $email = $_POST["email"];
    $senha = $_POST["senha"];

    $query = "INSERT INTO estudante (Nome, Email, Senha) VALUES ('$nome', '$email', '$senha')";

    mysqli_query($con, $query);
?>

