import java.util.Scanner;
import java.lang.Math;
public class prime_number {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		 try {
			 int N = input.nextInt();
			 for(int i=2; i<N;i++) {
				 
				 int count = 0;
				 
				 for(int j=1; j<=Math.sqrt(i); j++) {
					 if(i%j == 0) {
						 count = count+2;
					 }
				 }	
				 if(count ==2) {
					 System.out.print(i + " ");
				 }
			 }
		}
		 finally {
			 input.close();
		 }
	}
}
