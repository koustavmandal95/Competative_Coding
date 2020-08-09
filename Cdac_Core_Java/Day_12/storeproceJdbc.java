import java.util.*;
import java.sql.*;
public class storeproceJdbc {
	public static void main(String[] args) throws ClassNotFoundException, SQLException{
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/manufacturer", "root", "root");
		System.out.println("Connection got created with databases");
		Statement stmt = con.createStatement();
		
		CallableStatement cmt = con.prepareCall("{ call maxprice(?,?)}");
		System.out.println("options are Cosmetics , Retail , Battery , Power , Defence \n");
		Scanner input = new Scanner(System.in);
		
		String cname = input.next();
		
		cmt.setString(1,cname);
		cmt.registerOutParameter(2,Types.INTEGER);
		cmt.execute();
		System.out.println("The maximum price in "+cname+" is "+cmt.getInt(2));
		input.close();
	}
}