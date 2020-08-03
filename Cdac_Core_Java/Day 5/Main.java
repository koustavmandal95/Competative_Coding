
public class Main {
	public static void main(String[] args) {
		Author a = new Author("Robert Kiyosaki","richdad@gmail.com",'M');
		Book   b = new Book("Fake",700.3,100,a);
		b.display();
	}
}
