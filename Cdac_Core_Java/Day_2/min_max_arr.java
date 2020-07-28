import java.util.Scanner;

public class min_max_arr {
	public static int max(int arr[]) {
		int maximum = arr[0];
		for(int i=1;i<arr.length;i++) {
			if(arr[i] > maximum) {
				maximum = arr[i];
			}
		}
		return maximum;
	}
	public static int min(int arr[]) {
		int minimum = arr[0];
		for(int i=1;i<arr.length;i++) {
			if(arr[i] < minimum) {
				minimum = arr[i];
			}
		}
		return minimum;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the element");
		try {
			int n = input.nextInt();
			int arr[]=new int[n];
	        System.out.println("enter the values elements");
	        for(int i=0;i<n;i++){//for reading array
	            arr[i]=input.nextInt();
	        }
	       int Max = max(arr);
	       int Min = min(arr);
	       System.out.println("The Maximum is "+ Max);
	       System.out.println("The Minimum is "+ Min);
	}
	    finally {
        	input.close();
        }
	}
}
