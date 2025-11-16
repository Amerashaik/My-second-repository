def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
print(factorial(5)) # Output: 120

Dev-2 is adding anther code
import java.util.Scanner;
public class CheckEvenOdd {
   public static void main(String[] args) {
       Scanner reader = new Scanner(System.in);
       System.out.print("Enter a number: ");
       int num = reader.nextInt();
       if (num % 2 == 0)
           System.out.println(num + " is even");
       else
           System.out.println(num + " is odd");
   }
}
