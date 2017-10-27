import java.util.Scanner;
import java.util.Locale;

public class Main{
    public static void main(String[] args){
        Locale.setDefault(Locale.US);
        int num, maior = 0;

        Scanner sc = new Scanner(System.in);

        for(int i = 0; i < 3; i++){
            num = sc.nextInt();
            if(i == 0)
                maior = num;

            if(num > maior)
                maior = num;
                
        }


        System.out.printf("%d eh o maior\n", maior);

    }
}
