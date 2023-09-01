<?php
    $email = $_POST['email'];

    $tam = strlen($email);

    $mensagem = '';

    if($tam > 20) {
        $mensagem = 'maior';

    } else {
        $mensagem = 'menor';

    }

    $json = json_encode($mensagem);

    echo $json;
?>