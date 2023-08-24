function calcula() {
    var valor1 = parseInt(document.getElementById('valor1').value);
    var valor2 = parseInt(document.getElementById('valor2').value);
    var operacao = document.getElementById('operacao').value;

    if(operacao == '+') {
        var res = valor1 + valor2;
    }
    else if(operacao == '-') {
        var res = valor1 - valor2;
    }
    else if(operacao == '*') {
        var res = valor1 * valor2;
    }
    else if(operacao == '/'){
        var res = valor1 / valor2;
    }
    
    document.getElementById('res').value = res;
}