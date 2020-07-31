 class Person{
	public String name;
	public int age;
	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}
	void getDetails() {
		System.out.println("The name is "+ this.name+" & the age is "+  this.age );
	}
	
}
class Employee extends Person{
	public String profession;
	public Employee(String name, int age) {
		super(name,age);
	}
	void myprofession(String profession) {
		this.profession = profession;
	}
	void getProfession() {
		System.out.println("My Profession is "+this.profession);
	}
}
class Teacher extends Person{
	private String profession;
	public Teacher(String name, int age) {
		super(name, age);
	}
	void myprofession(String profession) {
		this.profession = profession;
	}
	void getProfession() {
		System.out.println("My Profession is "+this.profession);
	}
	
}
class PermanentEmp extends Employee{
	public PermanentEmp(String name, int age) {
		super(name, age);
		
	}
	@Override
	void myprofession(String profession) {
		// TODO Auto-generated method stub
		super.myprofession(profession);
	}
	
}
class ContractEmp extends Employee{

	public ContractEmp(String name, int age) {
		super(name, age);
	}
	void myprofession(String profession) {
		super.myprofession(profession);
	}
	
}
public class Persontest {
	public static void main(String[] args) {
		System.out.println("****************************************************************");
		Person p1 = new Person("Aakanksha Vasanth Magod",24);
		p1.getDetails();
		
		System.out.println("****************************************************************");
		Teacher t = new Teacher("Kanatha Ram",44);
		t.getDetails();
		t.myprofession("History Professor");
		t.getProfession();
		
		System.out.println("****************************************************************");
		PermanentEmp pe1 = new PermanentEmp("Karan Rana",33);
		pe1.myprofession("Junior Architect");
		pe1.getDetails();
		pe1.getProfession();
		
		System.out.println("****************************************************************");
		ContractEmp ce1 = new ContractEmp("Koustav",34);
		ce1.myprofession("software Developer");
		ce1.getDetails();
		ce1.getProfession();
		
		System.out.println("****************************************************************");
		
	}
}