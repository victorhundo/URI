import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        double nota1,nota2,media,peso1=0.35,peso2=0.75;

        Scanner sc = new Scanner(System.in);
        nota1 = sc.nextDouble();
        nota2 = sc.nextDouble();

        media = (nota1*peso1 + nota2*peso2)/(peso1 + peso2);

        System.out.printf("MEDIA = %.5f\n", media);

    }
}
