import java.util.Scanner;
public class Table {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter the number u want the table for ");
		Scanner input = new Scanner(System.in);
		try {
			int num = input.nextInt();
			for(int i=1;i<=10;i++) {
				System.out.println(num + " X " + i + " = "+ num*i);
			}
		}
		finally {
			input.close();
		}
	}
}
