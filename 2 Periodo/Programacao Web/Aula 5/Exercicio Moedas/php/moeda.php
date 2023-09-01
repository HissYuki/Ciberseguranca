<?php
    $pais = $_POST['pais'];
    $moeda = '';

    switch($pais) {
        case 'Brasil':
            $moeda = 'Real';
            break;
        
        case 'EUA':
            $moeda = 'Dolar Americano';
            break;

        case 'Japao':
            $moeda = 'Iene';
            break;
    }

    $moeda_json = json_encode($moeda);

    echo $moeda_json;
?>