import java.util.Scanner; 

class sub {
  public static void main(String[] args) {
    int x, y;
    int diff;
    Scanner scanner = new Scanner(System.in); 
    System.out.println("First number to add:");
    x = scanner.nextInt(); 

    System.out.println("Second number to add:");
    y = scanner.nextInt(); 

    diff = x - y; 
    System.out.println("The difference is: " + diff);
  }
} 