package Java1;
import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;

public class test2 {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        Random random = new Random();
        ArrayList<Integer> arrList = new ArrayList<Integer>();
        
        System.out.print("Введите количество случайных чисел: ");
        int n = scan.nextInt();
        for (int i = 0; i < n; i++) {
            int rand = random.nextInt(100); 
            System.out.println(rand); 
            arrList.add(rand);
        }
        System.out.print("Введите множитель: ");
        int a = scan.nextInt();
        for (int digit : arrList) {
            int res = digit * a; 
            System.out.println(res);
        }
    }   
}
