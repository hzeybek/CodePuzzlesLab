public class Q2StringPermutations {


    public static void main(String[] args) {
        System.out.println(checkStrings("Halil","lilaH"));
        System.out.println(checkStrings("Halil","Hallil"));
    }



    static boolean checkStrings(String word1, String word2){

        if (word1.length()!=word2.length()){
            return false;
        }
        int [] wordChars = new int[128];

        for(int i=0; i<word1.length();i++){
            int ascii = word1.charAt(i);
            wordChars[ascii] = wordChars[ascii]+1;
        }

        for(int i=0; i<word2.length();i++){
            int ascii = word2.charAt(i);
            wordChars[ascii] = wordChars[ascii]-1;

            if (wordChars[ascii]<0){
                return false;
            }

        }



        return true;
    }


}
