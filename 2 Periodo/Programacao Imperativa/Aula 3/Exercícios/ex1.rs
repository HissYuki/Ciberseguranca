/************************************************************************************************
Crie um programa em Rust que recebe como entrada a idade de um usuário e, se for maior de
idade, mostre na tela que ele é maior de idade. Caso contrário, mostre que ele é menor de idade.
************************************************************************************************/

use std::io;

fn main() {
    let mut idade: String = String::new();

    io::stdin().read_line(&mut idade).expect("Erro ao ler a entrada.");

    let idade_num: u8 = idade.parse().expect("Erro ao converter a variável: String -> u8");

    if idade_num >= 18 {
        println!("Você é maior de idade.");
    }
    else {
        println!("Você é menor de idade.");
    }
}