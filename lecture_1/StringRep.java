import java.util.Arrays;
public class StringRep {    
    public static void main(String[] args) {
        String str1 = "PHP";
        System.out.println("Original string: "+str1);
        String resultV1 = repeat_str(str1, 7);
       System.out.println("\nAfter repeating 7 times: "+resultV1);
   }
public static String repeat_str(String str1, int n) {
       if (str1 == null || str1.isEmpty()) {
           return "";
       }
       if (n <= 0) {
           return str1;
       }
       StringBuilder x = new StringBuilder(str1.length() * n);
       for (int i = 1; i <= n; i++) {
           x.append(str1);
       }
       return x.toString();
   }
}
