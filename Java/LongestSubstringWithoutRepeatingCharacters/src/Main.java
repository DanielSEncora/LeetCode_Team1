import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args){
        String s = "waxyoripwwkew";
        System.out.println(lengthOfLongestSubstring(s));
    }

    public static int lengthOfLongestSubstring(String s) {
        int max = 0;
        int izq = 0;

        Set<Object> charSet = new HashSet<>();

        //While loop that that iterates until we have done all possible combinations of substrings.
        while(izq < s.length()) {
            //Goes through each character of the String
            for (char chars : s.substring(izq).toCharArray()) {
                /*
                    Adds the character to the Set. If set.add returns false, then it saves the length of the set if it's superior than
                    the current max
                */
                if (!charSet.add(chars)) {
                    if (charSet.size() > max) {
                        max = charSet.size();
                    }
                    // Sums 1 to the izq value so that we can try again this time starting from the x+1 character.
                    izq++;
                    //Clears the set
                    charSet.clear();
                    //Re-starts the fore loop this time with distinct izq and max values.
                    break;
                }
            }
        }
        //Returns length of longest substring
        return max;
    }
}
