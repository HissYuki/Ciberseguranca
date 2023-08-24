/************************************************************************************
Escreva um programa em Rust para mostrar a sequência de Fibonacci até n termos
• Em seguida, some os termos pares da sequência e, ao final, mostre a soma
************************************************************************************/

use std::io;

fn main() {
    let mut tam: String = String::new();

    println!("Digite um número: ");
    io::stdin().read_line(&mut tam).expect("Erro ao ler a entrada!");

    let tam_num: u8 = tam.trim().parse().expect("Erro ao converter a variável: String -> u8");

    let mut fib: u8 = 1;
    let mut fib_ant: u8 = 0;
    let mut soma: u8 = 0;

    println!("Sequência de Fibonacci: ");

    for i in 0..tam_num {
        println!("{}", fib);

        if fib % 2 == 0 {
            soma += fib;
        }
        
        let aux: u8 = fib;
        fib += fib_ant;
        fib_ant = aux;
    }

    println!("\nSoma dos valores pares da sequência: {}", soma);

}