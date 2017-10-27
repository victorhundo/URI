import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        int km;

        Scanner sc = new Scanner(System.in);
        km = sc.nextInt();
        System.out.printf("%d minutos\n", km*2);

    }
}
