import java.util.Scanner;
public class reverse_arr {
	public static void rev_arr(int arr[]) {
		int mid = arr.length/2;
		int high = arr.length;
		int i = 1;
		int temp = 0;
		while(i <= mid) {
			temp = arr[i-1];
			arr[i-1] = arr[high-i];
			arr[high-i]=temp;
			i++;
		}
		System.out.println("The reverse array is " );
        for(int j=0;j<high;j++){//for reading array
            System.out.print(arr[j]+" ");
        }
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
	        rev_arr(arr);
	}
	    finally {
        	input.close();
        }

	}
}