// Estudante: Marco Aurelio Nissikawa Hisatomi

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        questao1();
        questao2();
        questao3();
    }

    public static void questao1() {
        System.out.println("Questão 1: Cálculo da área de um retângulo.");

        Scanner s = new Scanner(System.in);

        System.out.printf("Digite a base do retângulo: ");
        double base = s.nextDouble();

        System.out.printf("Digite a altura do retângulo: ");
        double altura = s.nextDouble();

        double area = base * altura;

        System.out.println("A área do retângulo é: " + area + "\n");
        
    }

    public static void questao2() {
        System.out.println("Questão 2: Conversão de temperatura.");

        Scanner s = new Scanner(System.in);

        System.out.printf("Digite a temperatura em graus Celsius: ");
        double celsius = s.nextDouble();

        double farenheit = (celsius * 9 / 5) + 32;

        System.out.println("A temperatura em graus Farenheit é: " + farenheit + "\n");
    }

    public static void questao3() {
        System.out.println("Questão 3: Calculadora.");
        
        Scanner s = new Scanner(System.in);

        System.out.printf("Digite o primeiro número: ");
        double num1 = s.nextDouble();

        System.out.printf("Digite o segundo número: ");
        double num2 = s.nextDouble();

        double soma = num1 + num2;
        double subtracao = num1 - num2;
        double multiplicacao = num1 * num2;
        double divisao = num1 / num2;

        System.out.println("Soma: " + soma);
        System.out.println("Subtração: " + subtracao);
        System.out.println("Multiplicação: " + multiplicacao);
        System.out.println("Divisão: " + divisao);
        s.close();
    }
}