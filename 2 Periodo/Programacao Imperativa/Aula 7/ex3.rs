/********************************************************************************
Crie uma função concatenar() que recebe duas Strings como parâmetro e retorne a
concatenação das duas. Considere o exemplo a seguir e os conceitos de ownership
para resolver.
********************************************************************************/

fn concatenar(str1: String, str2: String) -> String {
    let resultado1 = str1 + str2.as_str();
    resultado1
}


fn main() {
    let a: String = String::from("Olá!");
    let b: String = String::from("Mundo");
    let c: String = String::from("!");

    let resultado1 = concatenar(a, b);
    let resultado2 = concatenar(resultado1, c);
    println!("{}", resultado2);
}