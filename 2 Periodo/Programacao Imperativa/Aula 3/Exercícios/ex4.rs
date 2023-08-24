/************************************************************************************************
Escreva um programa em Rust que calcule a soma dos números ímpares em um intervalo de 0 até 100
************************************************************************************************/

fn main() {
    let mut soma: u16 = 0;

    for i in 0..100 {
        if i % 2 == 1 {
            soma += i;
        }
    }

    println!("Soma dos números ímpares de 0 até a 100: {}", soma);
}
