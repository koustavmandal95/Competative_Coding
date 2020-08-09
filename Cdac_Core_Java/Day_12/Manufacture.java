import java.sql.*;

public class Manufacture {
	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/manufacturer", "root", "root");
		System.out.println("Connection got created with databases");
		Statement stmt = con.createStatement();

		
		
		  String sql = "CREATE TABLE IF NOT EXISTS PRODUCT " + "(id INTEGER not NULL, " +
		  " name VARCHAR(255), " + " categoryName VARCHAR(255), " + " price INTEGER, "
		  + " manfacturerer VARCHAR(255) , " + " Quantity VARCHAR(255) , " +
		  " PRIMARY KEY ( id ))"; 
		  stmt.executeUpdate(sql);
		 
		System.out.println("Created table in given database...");
		

//		
//		String ins = "INSERT INTO Product "+
//					"VALUES (100,'Koustav','Cosmetics',456,'Lakme','1000')";
//		stmt.executeUpdate(ins);
		
//		stmt.executeUpdate("INSERT INTO product VALUES (101,'Sanjay','Retail',3344,'Pepsi',1230)");
//		stmt.execute("INSERT INTO product values (102,'Nippon','Battery',3764,'Exide',7345)");
//		stmt.execute("INSERT INTO product values (103,'Ratan','power',8731,'TataPower',1830)");
//		stmt.execute("INSERT INTO product values (104,'Kamal','Defence',390244,'DRDO',130)");
		
//		System.out.println("Records are inserted");
	
		stmt.execute("Update product set price = price - (5/100)*price where categoryName = 'power'");
		ResultSet rs1 = stmt.executeQuery("select  *,(quantity*price) as amount  from product");
		System.out.println("id"+" "+"name"+" "+"CName"+" "+"price"+" "+"manufurer"+" "+"Qty"+" "+"amount" );
		while(rs1.next())
		{
			System.out.println( rs1.getInt(1) +" "+rs1.getString(2)+" "+rs1.getString(3)+" "+rs1.getInt(4)+" "+rs1.getString(5)+" "+rs1.getInt(6)+" "+rs1.getInt(7));			
			}
		}
	}
	
