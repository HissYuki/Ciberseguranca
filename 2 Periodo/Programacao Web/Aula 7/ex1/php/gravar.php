<?php
    $title = $_POST["title"];
    $duration = $_POST["duration"];
    $composer = $_POST["composer"];
    $album = $_POST["album"];

    $connection = mysqli_connect("localhost:3306", "root", "PUC@1234", "pucpr");
    $query = "INSERT INTO musica (titulo, duracao, compositor, album) VALUES ('$title', $duration, '$composer', '$album')";

    mysqli_query($connection, $query);

?>