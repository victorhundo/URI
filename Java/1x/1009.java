import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        String nome;
        double vendas, salarioFixo, salario;

        Scanner sc = new Scanner(System.in);
        nome = sc.next();
        salarioFixo = sc.nextDouble();
        vendas = sc.nextDouble();

        salario = salarioFixo + (vendas*0.150);

        System.out.printf("TOTAL = R$ %.2f\n", salario);


    }
}
