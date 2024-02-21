if __name__ == '__main__':
    a = int(input("Digite o valor do primeiro termo da PA: "))
    r = int(input("Digite a razão da PA: "))
    n = int(input("Digite o número de termos da PA: "))

    t = a + (n-1) * r
    s = (a + t) * n/2
    print(f"Último termo da PA: {t}")
    print(f"Soma de todos os termos da PA: {s}")
