import java.util.Scanner;

	public class Second_highest {
		
		public static int max(int arr[]) {
			int maximum = arr[0];
			for(int i=1;i<arr.length;i++) {
				if(arr[i] > maximum) {
					maximum = arr[i];
				}
			}
			return maximum;
		}
		public static int secondHighest(int arr[]) {
			int ans = max(arr);
			int secondMax = arr[0];
			for(int i=1;i<arr.length;i++) {
				if(arr[i] > secondMax && arr[i]!= ans) {
					secondMax = arr[i];
				}
			}
			return secondMax;
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
	        int Smax = secondHighest(arr);
	        System.out.println("The second Highest is "+ Smax);
		}
		finally {
			input.close();
		}

		}
	}
