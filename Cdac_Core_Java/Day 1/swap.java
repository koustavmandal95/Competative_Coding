import java.util.*;
public class swap {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		try {
			System.out.println("Enter the value of a");
			int a = input.nextInt();
			System.out.println("Enter the value of b");
			int b = input.nextInt();
			b = a+b;
			a = b - a;
			b = b-a;
			System.out.println("The value of a : "+ a);
			System.out.print("The value of b : "+ b);
		}
	finally {
		input.close();
	}
 }
	
}
