import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        double nota1,nota2,nota3,media,peso1=0.2,peso2=0.3,peso3=0.5;

        Scanner sc = new Scanner(System.in);
        nota1 = sc.nextDouble();
        nota2 = sc.nextDouble();
        nota3 = sc.nextDouble();

        media = nota1*peso1 + nota2*peso2 + nota3*peso3;

        System.out.printf("MEDIA = %.1f\n", media);

    }
}
