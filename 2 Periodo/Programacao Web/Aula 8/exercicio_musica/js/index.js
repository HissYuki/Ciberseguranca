function gravar() {
    var form = document.getElementById("form");
    var dados = new FormData(form);

    fetch("php/gravar.php", {
        method: "POST",
        body: dados
    });
}

async function listar() {
    var retorno = await fetch("php/listar.php", {
        method: "GET"
    });

    var dados = await retorno.json();

    alert(Object.values(dados[1]));
}