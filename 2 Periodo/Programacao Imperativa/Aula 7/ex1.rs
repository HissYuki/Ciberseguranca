/******************************************************************************************************
Crie uma função que recebe uma string como parâmetro e retorne um usize que representa o tamanho dela.
(Não pode utilizar funções nativas do Rust)
******************************************************************************************************/

fn get_str_tam(string: &String) {
    let mut tam: usize = 0;

    for _ in string.as_bytes() {
        tam += 1;
    }

    tam
}

fn main() {
    let str: String = "Hello".to_string();
    println!("{:?}", get_str_tam(&str));
}