async function gravar() {
    var form = document.getElementById('formulario');
    var dados = new FormData(form);

    fetch('php/gravar.php', {
        method: "POST",
        body: dados
    });
}