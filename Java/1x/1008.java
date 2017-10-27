import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        int numero;
        double horas, valorHora, salario;

        Scanner sc = new Scanner(System.in);
        numero = sc.nextInt();
        horas = sc.nextDouble();
        valorHora = sc.nextDouble();

        salario = horas*valorHora;

        System.out.printf("NUMBER = %d\n", numero);
        System.out.printf("SALARY = U$ %.2f\n", salario);


    }
}
