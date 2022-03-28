
public class MyFirstApp8 {

	public static void main(String[] args) {
		// Make three sets of words to choose from. Add your own!!
		String[] wordListOne = {"24/7", "multi-tier", "30,000 foot", "B-to-B", "win-win", "front-end", "web-based", "persvasive", "smart", "six-sigma", "critical path", "dynamic"};
		String[] wordListTwo = {"empowered", "sticky", "value-added", "oriented", "centric", "disturbed", "clustered", "branded", "outside-the-box", "positioned", "networked", "focused", "leveraged", "aligned", "targeted", "shared", "cooperated", "accelerated"};
		String[] wordListThree = {"process", "tipping point", "solution", "architecture", "core competency", "stratergy", "mindshare", "portal", "space", "vision", "paradigm", "mission"};
		
		// Find out how many words are in each list. 
		int oneLength = wordListOne.length;
		int twoLength = wordListTwo.length;
		int threeLength = wordListThree.length;
		
		// Generate three random numbers. 
		int rand1 = (int) (Math.random() * oneLength);
		int rand2 = (int) (Math.random() * twoLength);
		int rand3 = (int) (Math.random() * threeLength);
		
		// Now build a phrase
		String phrase = wordListOne[rand1] + "" + wordListTwo[rand2]+ "" + wordListThree[rand3];
		
		// Print out the phrase. 
		System.out.println("What we need is a " + phrase);		
	}
}
