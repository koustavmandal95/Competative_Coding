import java.util.Scanner;

public class student {
	String name;
	int id;
	int marks;
		void initialize() {
			System.out.println("Enter the name,id,marks");
			Scanner input = new Scanner(System.in); 
			name = input.nextLine();
			id = input.nextInt();
			marks = input.nextInt();
	
	}
	void display() {
		System.out.println(name);
		System.out.println(id);
		System.out.println(marks);
	}
	public static void main(String args[]) {
		System.out.println("Number of Student record u wanna enter");
		Scanner number = new Scanner(System.in);
		int N = number.nextInt();
		student [] stud = new student[N];
		for(int i=0; i < N; i++) {
			stud[i] = new student();
			stud[i].initialize();
		}
		for(int i=0; i < N; i++) {
			stud[i].display();
		}

	}
}
