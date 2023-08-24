/*****************************************************************************
Escreva um programa em Rust que leia números inteiros do teclado. Quando
digitado o valor 0, o programa deverá encerrar e mostrar a média dos números
fornecidos de entrada.
*****************************************************************************/

use std::io;

fn main() {
    let mut input: String = String::new();

    println!("Digite um número: ");
    io::stdin().read_line(&mut input).expect("Erro ao ler a entrada.");

    let mut input_num: u16 = input.trim().parse().expect("Erro ao converter a variável: String -> u16");

    let mut soma: u32 = input_num as u32;
    let mut cont: u8 = 1;
    while input_num != 0 {
        println!("Digite um número: ");
        input = String::new();
        io::stdin().read_line(&mut input).expect("Erro ao ler a entrada.");

        input_num = input.trim().parse().expect("Erro ao converter a variável: String -> u16");
        soma += input_num as u32;
        cont += 1;
    }

    let media: u32 = soma / ((cont as u32) - 1);
    println!("Média dos números digitados: {}", media);
}