import java.util.Scanner;
public class factorial {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter the number");
		 Scanner myObj = new Scanner(System.in);
		 int n = myObj.nextInt();
		int answer =  1 ;
		while(n>0) {
		answer= answer*n;
			n--;
		}
		System.out.print("The factorial is "+answer);
		myObj.close();
	}
}
