
public class MyFirstApp7 {

	public static void main(String[] args) {
		int beerNum = 99;
		String word = "bottles";
		
		while (beerNum>0) {
			if(beerNum == 1) {
				word="bottle"; //Singular, as in one bottle.
			}
		System.out.println(beerNum + " " + word + " of beer on the wall. " );
		System.out.println(beerNum + " " + word + " of beer. ");
		System.out.println("Take one down.");
		System.out.println("Pass it around.");
		beerNum = beerNum - 1;
		
		if(beerNum > 0) {
			System.out.println(beerNum + " " + word + " of beer on the wall.");
		} else {
			System.out.println("No more bottles of beer on the wall.");
		} // End of else loop.
		} // End of while loop.
	} // End of main method.
} // End class. 

// Flaw in the code : println statement in if loop. It is worded wrong. 