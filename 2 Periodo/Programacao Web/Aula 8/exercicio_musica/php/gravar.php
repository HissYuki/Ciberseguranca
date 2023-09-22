<?php
    $titulo = $_POST["titulo"];
    $duracao = $_POST["duracao"];
    $compositor = $_POST["compositor"];
    $album = $_POST["album"];

    $conn = mysqli_connect("localhost:3306", "root", "PUC@1234", "pucpr");

    $query = "INSERT INTO musica (titulo, duracao, compositor, album) VALUES ('$titulo', '$duracao', '$compositor', '$album')";
    mysqli_query($conn, $query);
?>