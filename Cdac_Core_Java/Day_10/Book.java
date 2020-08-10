import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Map.Entry;
public class Book {
	String bookname;
	double price;
	String authorName;
	String isbnNo ;
	String publication;
	public Book(String name, double price, String authorName, String isbnNo, String publication) {
		this.bookname = name;
		this.price = price;
		this.authorName = authorName;
		this.isbnNo = isbnNo;
		this.publication = publication;
	}
	@Override
	public String toString() {
		return "Book Details [bookname=" + bookname + ", price=" + price + ", authorName=" + authorName + ", isbnNo=" + isbnNo
				+ ", publication=" + publication + "]";
	}
	public static void display(ArrayList<Book> al)
	{
		for(Book obj: al) {
			System.out.println(obj);
		}
	}
	public static HashMap<Integer,Object> addHashMap(ArrayList<Book> al) {
		HashMap<Integer, Object> mapObject = new HashMap<Integer,Object>();
		for(int i = 0 ; i < al.size(); i++) {
			mapObject.put(i,al.get(i));
		}
		return mapObject;
	}
	public static void displayMap(HashMap<Integer,Object> mapObj) {
		for(Map.Entry<Integer,Object> obj:mapObj.entrySet() )
		{
			System.out.println("Index "+obj.getKey()+ "--->"+ obj.getValue());
			
			
		}
	}
	public static void findBook(HashMap<Integer,Object> mapObj,int index) {
		for(Map.Entry<Integer,Object> obj:mapObj.entrySet() )
		{
			if(index == obj.getKey()) {
				System.out.println("\nBook found with index  "+obj.getKey()+ " is "+ obj.getValue());
			}
			
		}
	}
	public static void discount(ArrayList<Book> al,String publication)
	{
		System.out.println("\nThe 10% discounted Book details for publication "+publication);
		for(Book obj: al) {
			if(obj.publication.equalsIgnoreCase(publication)) {
				obj.price = obj.price - (0.1)*(obj.price);
				System.out.println(obj);
			}
		}
	}
}
 class Test{
	public static void main(String[] args) {
		Book b1 = new Book("Fake",700,"Robert Kiyosaki","22311111GB","Bestseller");
		Book b2 = new Book("Rich dad",570,"Robert Kiyosaki","22453111GB","Pearson");
		Book b3 = new Book("Love Evil",700,"Koustav Mandal","223111321GB","Prism");
		Book b4 = new Book("War",700,"Kavya Pathak","223118923GB","Sapna");
		Book b5 = new Book("Pension",650,"Ted Sidle","22319871GB","Bestseller");
		ArrayList<Book> al = new ArrayList<>();
		al.add(b1);
		al.add(b2);
		al.add(b3);
		al.add(b4);
		al.add(b5);
//		Book.display(al);
		
		HashMap<Integer,Object> mapObj = Book.addHashMap(al);
		Book.displayMap(mapObj);
		int index = 2;
		Book.findBook(mapObj,index);
		
		String publication = "BestSeller";
		Book.discount(al,publication);

	}
}