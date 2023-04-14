/* Description:
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

Link to the problem -> https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/java
*/


import java.util.HashMap;
import java.util.Map;

public class DuplicateEncoder {
    public static void main(String[] args) {
        /*
        "din"      =>  "((("
        "recede"   =>  "()()()"
        "Success"  =>  ")())())"
        "(( @"     =>  "))(("
        */
        System.out.println((stringSplit("din")));
        System.out.println((stringSplit("recede")));
        System.out.println((stringSplit("Success")));
        System.out.println((stringSplit("(( @")));
    }

    public static String stringSplit(String s) {
        s = s.toLowerCase();
        String result = "";
        Map<String, Integer> map = new HashMap<>();

        for (int idx=0;idx<s.length();++idx) {
            String c = String.valueOf(s.charAt(idx)));
            map.merge(c, 1, Integer::sum);
        }

        for (int idx=0;idx<s.length();++idx) {
            String c = String.valueOf(s.charAt(idx));
            if (map.get(c) == 1) {
                result += '(';
            }
            else {
                result += ')';
            }
        }
        return result;
    }
}