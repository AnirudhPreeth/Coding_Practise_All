// Be the compiler :

/*class Exercise1b {
public static void main(String [] args) {
int x = 1;
while ( x < 10 ) {
if ( x > 3) {
System.out.println(�big x�);
}
}
}
}
 */

public class MyFirstApp10 {

	public static void main(String[] args) {
		int x = 1;
		while(x < 10) {
			x =x+1;
			if(x>3) {
				System.out.println("big x");
			}
		}
	}

}

// No compilation. There is no x = x+1 statement in the while loop. 