/******************************************************************

******************************************************************/

fn palindromo(s: &String) {
    let s_reverse = s.chars().rev();

    for (c_orig, c_rev) in s.chars().zip(s_reverse) {
        if c_orig != c_rev {
            return false;
        }
    }

    true
}

fn main() {
    let s: String = String::from("marco");

    print("{}", palindromo(&s));
}