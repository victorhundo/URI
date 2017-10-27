import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        int segundos, minutos, horas;

        Scanner sc = new Scanner(System.in);
        segundos = sc.nextInt();
        
        horas = segundos/3600;
        minutos = (segundos%3600)/60;
        segundos = (segundos%3600)%60;

        System.out.printf("%d:%d:%d\n",horas, minutos, segundos);

    }
}
