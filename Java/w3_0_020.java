import java.util.Scanner;
public class w3_0_020{
    public static void main(String[] args){
        int numIn;
        Scanner scan = new Scanner(System.in);
        System.out.print("Input a decimal number: ");
        numIn = scan.nextInt();
        System.out.print("Hexadecimal number is: "+Integer.toHexString(numIn));
        System.out.println("\nEND\n");
    }
}