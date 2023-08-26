/*************************************************************************
Crie um função que receba um vetor como parâmetro e retorne a sua média.
*************************************************************************/

fn media_vetor(v: Vec<f32>) -> f32 {
    let tam: f32 = v.len() as f32;
    let mut media: f32 = 0.0;
    for i in v {
        media += i;
    }

    media / tam
}

fn main() {
    let v: Vec<f32> = vec![2.0, 2.0];

    println!("{}", media_vetor(v));
}
