import java.util.Scanner;
public class w3_0_017{
    public static void main(String[] args){
        String bStr1;
        String bStr2;
        Scanner scan = new Scanner(System.in);
        System.out.print("\nInput first binary number: ");
        bStr1 = scan.next();
        System.out.print("\nInput second binary number: ");
        bStr2 = scan.next();
        System.out.println("\nSum of two binary numbers: "+(Integer.toBinaryString(Integer.parseInt(bStr1,2)+Integer.parseInt(bStr2,2))));
    }
}