/*********************************************************************************************
1. Escreva um algoritmo em Rust para calcular a idade de alguém, sabendo seu ano de nascimento
**********************************************************************************************/

use std::io;

fn main() {
    let mut ano: String = String::new();

    println!("Digite a sua idade: ");
    io::stdin().read_line(&mut ano).expect("Erro ao ler a linha.");

    let ano_num: u16 = ano.trim().parse().expect("Erro ao converter o número.");

    let idade:u8 = (2023 - ano_num) as u8;

    println!("Sua idade é {idade}");
}