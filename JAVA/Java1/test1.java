package Java1;
import java.util.Scanner;
public class test1 {
    public static void main(String[] args) {

        int[] cubes = new int[1000];

        for (int i = 1; i <= 1000; i++) {
            cubes[i-1] = i * i * i;
        }

        Scanner scan = new Scanner(System.in);

        System.out.println("Введите первое число из диапазона от 1 до 1000:");
        int a = scan.nextInt();

        System.out.println("Введите второе число из диапазона от 1 до 1000:");
        int b = scan.nextInt();

        int cubeA = cubes[a-1];
        int cubeB = cubes[b-1];

        System.out.println("Куб числа " + a + ": " + cubeA);
        System.out.println("Куб числа " + b + ": " + cubeB);
    }
}
