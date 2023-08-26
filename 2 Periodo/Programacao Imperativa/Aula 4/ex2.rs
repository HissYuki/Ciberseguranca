/*******************************************************************************
Crie uma função que calcule o fatorial de um número fornecido como parâmetro.
*******************************************************************************/

fn factorial(n: u32) -> u32 {
    if n==0 {
        return 1
    }

    factorial(n-1) * n
}

fn main() {
    let n: u32 = 5;

    println!("{}", factorial(n));
}