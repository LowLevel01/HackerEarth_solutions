import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
	    int t = sc.nextInt();//here goes nbr of test cases
	    while (t > 0) {
	      int n = sc.nextInt();
	      int k = sc.nextInt();
	      int[] arr = new int[n];
	      for (int i = 0; i < n; i++) {//copy the array from inputs
	        arr[i] = sc.nextInt();
	      }
	      k = k % n;
	      int rot = 0;
	      int[] rot_arr = new int[n];
	      for (int i = 0; i < n; i++) {
	    	rot = (i+k)%n;
	        rot_arr[rot] = arr[i];
	      }
	      for (int i = 0; i < n; i++) {
	        System.out.print(rot_arr[i] + " ");
	      }
	      t--;
	    }
	    sc.close();
	  }






	}


