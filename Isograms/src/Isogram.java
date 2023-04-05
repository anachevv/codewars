/* Description:
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false

Link to the problem -> https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/java
*/

import java.util.ArrayList;
import java.util.Collections;
import java.util.Objects;

public class Isogram {
    public static boolean isIsogram(String str) {
        str = str.toLowerCase();

        if (Objects.equals(str, "")) {
            return true;
        }

        ArrayList<Character> letters = new ArrayList<>();

        for (int i = 0; i < str.length(); i++) {
            letters.add(str.charAt(i));
            if (Collections.frequency(letters, str.charAt(i)) > 1) {
                return false;
            }
        }
        return true;
    }
}
