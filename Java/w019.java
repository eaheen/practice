import java.util.Scanner;
public class w019{
    public static void main(String[] args){
        int numIn;
        Scanner scan = new Scanner(System.in);
        System.out.print("Input a decimal: ");
        numIn = scan.nextInt();
        System.out.print("Binary number is: "+Integer.toBinaryString(numIn));
        System.out.println("\nEND\n");
    }
}
