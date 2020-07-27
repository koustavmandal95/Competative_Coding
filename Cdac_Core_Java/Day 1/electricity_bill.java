
/**
 * @author Koustav
 *
 */
import java.util.Scanner;
public class electricity_bill {

	/*
	 < = 100			Rs.1.20
	for the next 200 units 	Rs. 2.00
	for the next 300 units	Rs. 3.00
	for more after 500 units		Rs. 5.00		
	ex:  input = 320 units output = 100*1.20 +200*2.00+20*3.00 =  Rs. 580

	 */
public static void main(String[] args) {
		// TODO Auto-generated method stub
			System.out.print("The units used is :-");
			Scanner input = new Scanner(System.in);
			try {
				long units = input.nextLong();
				double Amt = 0.0;
				if(units <= 100) {
					Amt = units*1.20;
				}
				else if(units > 100 && units <=300) {
					Amt = 100*1.20 + (units -100)*2.00;
				}
				else if(units >300 && units <=500) {
					Amt = 100*1.20 + 200*2.00 + (units-300)*3.00;
				}
				else if(units >500) {
					Amt = 100*1.20 + 200*2.00 + 300*3.00+(units-500)*5.0;
				}
				System.out.println("The bill is "+ Amt);
				
			}
			finally {
				input.close();
			}
	}

}
