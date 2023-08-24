/************************************************************************************
Crie um programa para autenticar um usuário. Solicite o nome de usuário e senha e,
em seguida, verifique se o nome de usuário é “admin” e a senha é “@dm1n”. Caso a
senha ou o usuário não corresponderem, mostre na tela que o usuário ou a senha estão
incorretos. Caso contrário, mostre que o usuário foi autenticado.
************************************************************************************/


use std::io;

fn main() {
    let mut usuario: String = String::new();
    let mut senha: String = String::new(); 

    println!("Digite o usuário: ");
    io::stdin().read_line(&mut usuario).expect("Erro ao ler o usuário.");

    println!("Digite a senha: ");
    io::stdin().read_line(&mut senha).expect("Erro ao ler a senha.");

    let mut cont: u8 = 1;

    while usuario.trim() != "admin" && senha.trim() != "@dm1n" {
        cont += 1;
      
        if cont > 5 {
            println!("Limite de tentativas excedido. Fechando a aplicação.");
            break;
        }
        println!("Tentativa: {cont} / Máximo: 5");
      
        println!("Usuário não autenticado! \nTente novamente.");

        println!("Digite o usuário: ");
        io::stdin().read_line(&mut usuario).expect("Erro ao ler o usuário.");

        println!("Digite a senha: ");
        io::stdin().read_line(&mut senha).expect("Erro ao ler a senha.");
    }

    if cont < 5 {
      println!("Usuário autenticado!");
    }

}