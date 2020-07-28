public class arrayExample {
	/*
	 you can assign/store similar data to a single variable 
	 	--- elements are same Type
	 	--- referred by Index
	 	--- size is fixed
	 	--- length 
	 	--- elements stored on continues memory 
	 	int n[] = new int[4]
	 */
	public static void findTotal(int mark[]) {
		int total = 0;
		for(int i =0; i<mark.length;i++) {
			total+=mark[i];
		}
		System.out.println("The total is " + total);
		
	}
	public static void main(String[] args) {
		int[] n = new int[5];
		int val = 10;
		for(int i =0; i<5;i++) {
			n[i] = val;
			val = val+10;
		}
		 
		for(int i = 0; i<5; i++) {
			System.out.print(n[i]+" ");
		}
		int[] mark = {11,22,33,44,55};
		for(int i = 0; i<5; i++) {
			System.out.println("mark "+i +" "+mark[i] );
		}
		String[] sub = {"C++","dbt","java","python"};
		System.out.println("Iterating through each");
		for(String ele:sub) {
			System.out.println(ele);
		}
		findTotal(mark);
	}
}
