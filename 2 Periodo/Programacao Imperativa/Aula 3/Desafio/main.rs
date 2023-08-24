/******************************************************************************************************
Programação Imperativa - Desafio                    Professor: Pedro Horchulhack    Data: 18/08/2023
Autor: Marco Aurelio Nissikawa Hisatomi             Curso: Cibersegurança           Turma: Noite/U2
******************************************************************************************************/

use std::io;

fn main() {
    let mut n: String = String::new();

    println!("Digite um número inteiro positivo: ");
    io::stdin().read_line(&mut n).expect("Erro ao ler a entrada.");

    let n_number: u16 = n.trim().parse().expect("Erro ao converter a variável: String -> u8.");

    let mut soma_q: u16 = 0;
    let mut quadrado_s: u16 = 0;

    for i in 1..n_number+1 {
        soma_q += i*i;
        quadrado_s += i;
    }

    quadrado_s = quadrado_s * quadrado_s;

    let diff: u16 = quadrado_s - soma_q;

    println!("{} - {} = {}", quadrado_s, soma_q, diff);
}