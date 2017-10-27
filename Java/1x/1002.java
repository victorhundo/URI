import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        double PI = 3.14159, raio, area;
        
        Scanner sc = new Scanner(System.in);
        raio = sc.nextDouble();
        
        area = PI * raio * raio;
        System.out.printf("A=%.4f\n", area);
  }
}
