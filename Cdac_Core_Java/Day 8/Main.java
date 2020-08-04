package Forex;
import java.util.*;
public class Main {
	public static void main(String[] args) {
		BankAccount a = new BankAccount(2222,1000);
		float bal = a.currentBalance();
		System.out.println("Enter the choice  Press :-\n 1 --> Rupees \n 2 --> Dollars \n 3 --> Pounds \n 4 --> quit");
		Scanner input = new Scanner(System.in);
		while(true) {
			int choice = input.nextInt();
			if(choice ==4) {
				System.out.println("Exiting...");
				break;
			}
			switch(choice) {
			case 1:
				Rupees R = new Rupees(bal);
				System.out.println("The Avalable Balance is "+R.currentBalance() +" Rs");
				break;
			case 2:
				Dollars D = new Dollars(bal);
				System.out.println("The Avalable Balance is "+D.currentBalance() +"$");
				break;
			case 3:
				Pounds P = new Pounds(bal);
				System.out.println("The Avalable Balance is "+P.currentBalance() +'\u00A3');
				break;
			}
		}

	}

}
