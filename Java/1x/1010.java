import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        double codigoP1, numP1, valorP1;
        double codigoP2, numP2, valorP2;
        double total;

        Scanner sc = new Scanner(System.in);

        codigoP1 = sc.nextDouble();
        numP1 = sc.nextDouble();
        valorP1 = sc.nextDouble();

        codigoP2 = sc.nextDouble();
        numP2 = sc.nextDouble();
        valorP2 = sc.nextDouble();

        total = numP1*valorP1 + numP2*valorP2;
        
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", total);


    }
}
