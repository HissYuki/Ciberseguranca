/*********************************************************************************************
2. Escreva um algoritmo em Rust para calcular o valor, em reais, que deve ser pago para um 
cliente de uma locadora de carros. Sabe-se que:
1. O valor da locação para cada carro é 100.00 reais;
2. O cliente pode locar um único carro por vários dias;
**********************************************************************************************/

use std::io;

fn main() {
    let mut days: String = String::new();

    println!("Digite o número de dias locados pelo cliente: ");
    io::stdin().read_line(&mut days).expect("Erro ao ler a entrada.");

    let days_num: u8 = days.trim().parse().expect("Erro ao converter o número de carros.");
    let price: u16 = (days_num as u16) * 100;

    println!("O preço final será de {price}.");
}