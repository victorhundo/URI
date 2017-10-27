import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        double tempo, velocidade, distancia, litros;

        Scanner sc = new Scanner(System.in);
        tempo = sc.nextDouble();
        velocidade = sc.nextDouble();
        distancia = tempo * velocidade;
        litros = distancia/12;
        System.out.printf("%.3f\n", litros);

    }
}
