import java.util.HashMap;

public class App {

    public static void main(String[] args) {
        //To check if the given string has all unique characters
        String input = "Abcdef";
        System.out.println(isUniqueChars(input));

    }


    static boolean isUniqueChars(String input){
        boolean[] check = new boolean[128];

        for (int i=0; i<input.length();i++){
            int ascii_char = input.charAt(i);
            if (check[ascii_char]){
                return false;
            }
            check[ascii_char]=true;
        }


        return true;

    }
}
