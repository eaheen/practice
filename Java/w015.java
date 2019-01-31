public class w015{
    public static void main(String[] args){
        int a = 1;
        int b = 2;
        int c;
        System.out.printf("\nint a = %d\nint b = %d\n",a,b);
        c = a; a = b; b = c; c = 0;
        System.out.printf("\nSWAP\n\nint a = %d\nint b = %d\n",a,b);
    }
}
