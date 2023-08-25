function cadastrar() {
    var form = document.getElementById('formCadastro');
    var dados = new FormData(form);
    var flag_dados = true;

    for(const i of dados){
        if(i[1] == ""){
            flag_dados = false;
            break;
        }
    }

    if(dados["senha"])

    if(dados_preenchidos){
        fetch("php/gravar.php", {
            method: "POST", 
            body: dados
        })
    }
}