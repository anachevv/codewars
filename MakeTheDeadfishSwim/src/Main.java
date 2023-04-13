/*Description:
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

Deadfish.parse("iiisdoso") =- new int[] {8, 64};

Link to the problem -> https://www.codewars.com/kata/51e0007c1f9378fa810002a9
*/

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        String s = "iiisdoso";
        System.out.println(Arrays.toString(parse(s)));
    }

    public static int[] parse(String s) {
        int value = 0;
        int oCounter = 0;
        for (int idx = 0; idx < s.length(); ++idx) {
            char c = s.charAt(idx);
            if (c == 'o') {
                ++oCounter;
            }
        }
        int[] arr = new int[oCounter];
        int currO = -1;
        for (int idx = 0; idx < s.length(); ++idx) {
            char c = s.charAt(idx);
            switch (c) {
                case 'i' -> ++value;
                case 'd' -> --value;
                case 's' -> value *= value;
                case 'o' -> {
                    ++currO;
                    arr[currO] = value;
                }
            }
        }
        return arr;
    }
}
