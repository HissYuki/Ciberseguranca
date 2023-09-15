function gravar() {
    var form = document.getElementById('form');
    var dados = new FormData(form);

    fetch('php/gravar.php', {
        method: "POST",
        body: dados
    });
}