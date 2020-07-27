import java.util.*;
public class swtcase {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter ur choice form 1 to 9");
		Scanner input = new Scanner(System.in);
		try {
			int N = input.nextInt();
			switch(N) {
			case 1:
				System.out.println("One");
			break;
			case 2:
				System.out.println("Two");
			break;
			case 3:
				System.out.println("Three");
			break;
			case 4:
				System.out.println("Four");
			break;
			case 5:
				System.out.println("Five");
			break;
			case 6:
				System.out.println("Six");
			break;
			case 7:
				System.out.println("Seven");
			break;
			case 8:
				System.out.println("Eight");
			break;
			case 9:
				System.out.println("Nine");
			break;
			default:
				System.out.println("Invalid");
			
			}
			
		}
		finally {
			input.close();
		}
	}

}
