import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        double x1, x2, y1, y2, distancia;

        Scanner sc = new Scanner(System.in);
        x1 = sc.nextDouble();
        y1 = sc.nextDouble();

        x2 = sc.nextDouble();
        y2 = sc.nextDouble();

        double qx = Math.pow( (x2-x1), 2);
        double qy = Math.pow( (y2-y1), 2);
        distancia = Math.sqrt(qx + qy);

        System.out.printf("%.4f\n",distancia);

    }
}
