import java.util.Scanner;
public class largest_of_three {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("enter the three numbers \n");
		Scanner input = new Scanner(System.in);
		try {
			long  a = input.nextLong();
			long  b = input.nextLong();
			long  c = input.nextLong();
			if(a>b && a>c) {
				System.out.println("The Greatest is "+a);
			}
			else if(b>c && b>a) {
				System.out.println("The Greatest is "+b);
			}
			else if(c>a && c>a) {
				System.out.println("The Greatest is "+c);
			}
		}
		finally {
			input.close();
		}
	}

}
