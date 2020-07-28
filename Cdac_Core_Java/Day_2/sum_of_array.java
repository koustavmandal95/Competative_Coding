import java.util.*;
public class sum_of_array {
	public static void totalsum(int arr []) {
		int total = 0;
		for(int i =0; i<arr.length;i++) {
			total+=arr[i];
		}
		System.out.println("The total is " + total);
	}
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the element");
		try {
			int n = input.nextInt();
			int arr[]=new int[n];
	        System.out.println("enter the values elements");
	        for(int i=0;i<n;i++){//for reading array
	            arr[i]=input.nextInt();
	        }
	        totalsum(arr);
		}
		finally {
			input.close();
		}

	}

}
