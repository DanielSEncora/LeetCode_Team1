import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class main {
    public static void main(String[] args) {
        String s = "abd";
        String p = "a*b*c*d";


        System.out.println(isMatch(s,p));
    }

    public static boolean isMatch(String s, String p){
        Pattern pattern = Pattern.compile(p);
        Matcher matcher = pattern.matcher(s);

        return matcher.matches();
    }


}
