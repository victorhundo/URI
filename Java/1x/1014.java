import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        double km, litros, kmPorLitros;

        Scanner sc = new Scanner(System.in);
        km = sc.nextDouble();
        litros = sc.nextDouble();

        kmPorLitros = km/litros;

        System.out.printf("%.3f km/l\n", kmPorLitros);

    }
}
