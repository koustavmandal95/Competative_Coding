import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
public class Player {
	String name;
	int run;
	int wickets;
	int matches ;
	int no_of_century;
	String  category = null;
	public Player(String name, int run, int wickets, int matches, int no_of_century) {
		this.name = name;
		this.run = run;
		this.wickets = wickets;
		this.matches = matches;
		this.no_of_century = no_of_century;
		this.category = null;
	}
	public String getName() {
		return name;
	}
	@Override
	public String toString() {
		return " [name=" + name + ", run=" + run + ", wickets=" + wickets + ", matches=" + matches
				+ ", no_of_century=" + no_of_century + ", "+category + "]";
	}
	public static void display(ArrayList<Player> players) {
		for(Player obj: players) {
			System.out.println(obj);
		}
	}
	public static void maxrun( ArrayList<Player> players) {
		int max = 0;
			for(int i=0; i<players.size();i++) {
				if(max < players.get(i).run) {
					max = players.get(i).run;
				}
		}
			for(Player obj : players) {
				if(obj.run == max) {
					System.out.println("\n-----The details of higest run getters ----");
					System.out.println(obj);
				}
			}
			
	}
	public static void sortedByName(ArrayList <Player> players) {
		Collections.sort(players, Comparator.comparing(Player::getName));
		System.out.println("\nThe order list by Name as follows ---");
		for(Player obj: players) {
			System.out.println(obj);
		}
	}
	
	public static void remove(ArrayList <Player> players) {
		int pos = 0;
		for(int i =0 ; i < players.size(); i++) {
			if(players.get(i).run < 100 && players.get(i).matches > 3) {
				pos = i;
				System.out.println("\n -------The removed obj--------\n "+players.get(pos));
				players.remove(pos);
			}
		}
	}
	public static void Group(ArrayList <Player> players) {
		for(Player obj : players) {
			if(obj.no_of_century >= 10 ) {
				obj.category = "A";
			}
			else {
				obj.category = "B";
			}
		}
		System.out.println("********************************************8");
		display(players);
	}
}
class TestMain{
	public static void main(String[] args) {
		Player p1 = new Player("Koustav",7809,500,200,50);
		Player p2 = new Player("Akash",789,300,240,9);
		Player p3 = new Player("Zaheer",80,200,400,0);
		Player p4 = new Player("Virat",10809,500,176,65);
		Player p5 = new Player("Kaif",7829,100,45,12);
		
		ArrayList<Player> players = new ArrayList<>();
		
		players.add(p1);
		players.add(p2);
		players.add(p3);
		players.add(p4);
		players.add(p5);
		

		Player.display(players);
		Player.maxrun(players);
		Player.sortedByName(players);
		Player.remove(players);
		Player.Group(players);
		
	}
}
