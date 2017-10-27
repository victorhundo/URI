import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        double PI = 3.14159;
        double raio, volume;

        Scanner sc = new Scanner(System.in);
        raio = sc.nextDouble();

        volume = (4/3.0) * PI * raio * raio * raio;
        System.out.printf("VOLUME = %.3f\n", volume);


    }
}
