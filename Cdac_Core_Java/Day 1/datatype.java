import java.util.Scanner;
public class datatype {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
	    Scanner input = new Scanner(System.in);
		try {

		    System.out.println("Enter name, age and salary:");

		    // String input
		    String name = input.nextLine();

		    // Numerical input
		    int age = input.nextInt();
		    double salary = input.nextDouble();

		    // Output input by user
		    System.out.println("Name: " + name);
		    System.out.println("Age: " + age);
		    System.out.println("Salary: " + salary);
		  }
		

	finally {
		  input.close();
	}
	}
}
