package Java1;
import java.util.Scanner;
public class test3 {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        System.out.println("Введите первое число:");
        int num1 = scan.nextInt();

        System.out.println("Введите второе число:");
        int num2 = scan.nextInt();

        System.out.println("Выберите операцию (+, -, *, /):");
        char operation = scan.next().charAt(0);

        int result = 0;

        switch (operation) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                result = num1 / num2;
                break;
            default:
                System.out.println("Некорректная операция");
                break;
        }

        System.out.println("Результат: " + num1 + operation + num2 +"=" + result);
    }
}