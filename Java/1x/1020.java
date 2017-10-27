import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        int dias, meses, anos;

        Scanner sc = new Scanner(System.in);
        dias = sc.nextInt();
        
        anos  = dias/365;
        meses = (dias%365)/30;
        dias = (dias%365)%30;

        System.out.printf("%d ano(s)\n",anos);
        System.out.printf("%d mes(es)\n",meses);
        System.out.printf("%d dia(s)\n",dias);

    }
}
