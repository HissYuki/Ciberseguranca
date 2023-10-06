window.onload = async function() {
    var promise = await fetch("php/listar-app.php", {
        method: "GET"
    });

    var dados = await promise.json();

    for(var i = 0; i < dados.length; i++) {
        var conteudo = 
        `<div class="card">
            <div class="card-icon">
                <img src="img/twitter.png" width="40" />
            </div>
            <div class="card-titulo"> ${dados[i].nome} </div>
            <div class="card-desc"> ${dados[i].des} </div>
            <div class="card-botao">
                <button> READ MORE </button>
            </div>
        </div>`;

        document.getElementById('aplicativos').innerHTML += conteudo;

    }
}