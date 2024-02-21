import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Digite o valor do primeiro termo da PA: ");
        float a = s.nextFloat();

        System.out.println("Digite o valor da razão da PA: ");
        float r = s.nextFloat();

        System.out.println("Digite o número de termos da PA: ");
        float n = s.nextFloat();

        s.close();

        float t = a + (n - 1) * r;
        float soma = (a + t) * n/2;

        System.out.println("Último termo da PA: " + t);
        System.out.println("Soma de todos os termos da PA: " + soma);
    }
}