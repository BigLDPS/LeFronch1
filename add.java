import java.util.Scanner; 

class add {
  public static void main(String[] args) {
    int x, y;
    int sum;
    Scanner scanner = new Scanner(System.in); 
    System.out.println("First number to add:");
    x = scanner.nextInt(); 

    System.out.println("Second number to add:");
    y = scanner.nextInt(); 

    sum = x + y; 
    System.out.println("Sum is: " + sum);
    scanner.close();
  }
} 