/*********************************************************************************************
3. Leia a temperatura do teclado em Celsius e imprima o equivalente em Fahrenheit
**********************************************************************************************/

use std::io;

fn main() {
    let mut temp_celsius: String = String::new();

    println!("Digite a temperatura em graus celsius.");
    io::stdin().read_line(&mut temp_celsius).expect("Erro ao ler a entrada.");

    let temp_celsius_num: f64 = temp_celsius.trim().parse().expect("Erro ao converter a temperatura para ponto flutuante.");

    let temp_farenheint_num: f64 = (temp_celsius_num * 9.0)/5.0 + 32.0;

    pritln!("A temperatura em graus Farenheint é {temp_farenheint_num}.");
}