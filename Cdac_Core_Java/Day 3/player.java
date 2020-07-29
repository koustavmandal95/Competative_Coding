import java.util.Scanner;

public class player {
	String name;
	int age;
	String country;
	int run;
	static void runTally(player players[]) {
		System.out.println("The details of player more than 5000 runs");
		for( int i = 0; i < players.length ; i++) {
			if(players[i].run > 5000) {
				System.out.println(players[i].name);
				System.out.println(players[i].age);
				System.out.println(players[i].country);
				System.out.println(players[i].run);
			}
		}
	}
	void setRecords() {
		System.out.println("Enter the details --");
		Scanner  input = new Scanner(System.in);
		 name = input.nextLine();
		 age = input.nextInt();
		 country = input.next();
		 run = input.nextInt();
		
	}
	void display() {
		System.out.println(name);
		System.out.println(age);
		System.out.println(country);
		System.out.println(run);
	}
	
	public static void main(String args[]) {
		System.out.println("Enter the number of players");
		Scanner P = new Scanner(System.in);
		int N = P.nextInt();
		player[] players = new player[N];
		for(int i=0; i<players.length ; i++) {
			players[i] = new player();
			players[i].setRecords();
		}
//		players[0].display();
//		players[1].display();
		player.runTally(players);
		P.close();

	}
}
/*
virat kohli
22
India
10003
---
Rohit
27
West Indies
3833
-----
Chris 
34
westIndies
37890
-----
Cook
34
england
536
----
Sachin Tendulkar
40
India
33949
 */

