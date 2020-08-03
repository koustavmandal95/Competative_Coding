public class Book {
	private String name;
	private double price;
	private int qty;
	private Author author;
	public Book(String name, double price, int qty,Author author) {
		this.name = name;
		this.price = price;
		this.qty = qty;
		this.author = author;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}
	public int getQty() {
		return qty;
	}
	public void setQty(int qty) {
		this.qty = qty;
	}
	public Author getAuthor() {
		return author;
	}
	public void display() {
		System.out.println(name + " by "+author.getName() + " gender is "+author.getGender() 
		+" email at "+author.getEmail());
	}
}

