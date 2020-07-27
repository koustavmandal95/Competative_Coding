import java.util.*;
public class sum_of_digit {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter the digit");
		Scanner input = new Scanner(System.in);
		try {
			int  n = input.nextInt();
			int sum=0;
			while(n>0) {
				 sum = sum+n%10;
				n=n/10;
			}
			System.out.println("The sum is "+sum);
		}
		finally {
			input.close();
		}

	}

}
