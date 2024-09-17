import java.util.Scanner; 

public class pleasegivemeanA {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); 

        
        System.out.println("How many times would you like to hear my plea?");
        
        
        int x = scanner.nextInt(); 
        scanner.close();

       
        for(int y = 0; y < x; y++){
            System.out.println("PLEASE GIVE ME AN A");
        }
    }
}
