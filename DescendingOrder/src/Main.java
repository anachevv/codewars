/* Description:
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

Link to the problem -> https://www.codewars.com/kata/5467e4d82edf8bbf40000155/
*/

import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        System.out.println(sortDesc(42145));
        System.out.println(sortDesc(145263));
        System.out.println(sortDesc(123456789));
    }

    public static int sortDesc(final int number) {
        int size = Integer.toString(number).length();
        Integer[] values = new Integer[size];
        String temp = Integer.toString(number);
        for (int i=0;i<size;++i) {
            values[i] = temp.charAt(i) - '0';
        }
        Arrays.sort(values, Collections.reverseOrder());
        String result = "";
        for (int idx=0;idx<size;++idx) {
            result += values[idx];
        }
        return Integer.parseInt(result);
    }
}
