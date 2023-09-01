async function moeda() {
    var form = document.getElementById('form_pais');
    var dados = new FormData(form);

    var promise = await fetch('php/moeda.php', {
        method: 'POST',
        body: dados
    });

    var moeda_retorno = await promise.json();

    alert(moeda_retorno);
}