import java.util.*;
public class Pyramid {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter the number u want pyramid ");
		Scanner input = new Scanner(System.in);
		try {
			int n = input.nextInt() ;
			for(int i=0;i<=n;i++) {
				for(int j=0;j<i;j++) {
					System.out.print("*");
				}
				System.out.println();
			}
			for(int i=n;i>=0;i--) {
				for(int j=0;i>j;j++) {
					System.out.print("*");
				}
				System.out.println();
			}	
		}
		finally {
			input.close();
		}

	}
}
