import java.util.Scanner;
public class w3_0_007{
    public static void main(String[] args){
        int inputNum = 1;
        Scanner scan = new Scanner(System.in);
        System.out.print("Input a number: ");
        inputNum = scan.nextInt();
        int i;
        for(i=1;i<=10;i++){ 
            System.out.printf("\n%2d x %2d = %2d",inputNum,i,inputNum*i);
        }
        System.out.println("\nEND");
    }
}