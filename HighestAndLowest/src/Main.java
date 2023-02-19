// Description:
//In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
//
//        Examples
//        highAndLow("1 2 3 4 5")  // return "5 1"
//        highAndLow("1 2 -3 4 5") // return "5 -3"
//        highAndLow("1 9 3 4 -5") // return "9 -5"
//        Notes
//        All numbers are valid Int32, no need to validate them.
//        There will always be at least one number in the input string.
//        Output string must be two numbers separated by a single space, and highest number is first.
//
// Link to the problem -> https://www.codewars.com/kata/554b4ac871d6813a03000035

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        System.out.println(highAndLow("6"));
        System.out.println(highAndLow("30"));
        System.out.println(highAndLow("-23"));
        System.out.println(highAndLow("-5"));
        System.out.println(highAndLow("1 2 3 4 5"));
        System.out.println(highAndLow("1 2 -3 4 5"));
        System.out.println(highAndLow("1 9 3 4 -5"));
        System.out.println(highAndLow("-5 -3 -9 41 40 42"));
    }
    public static String highAndLow(String numbers) {
        String[] strArr = numbers.split(" ");
        int[] arr = new int[strArr.length];

        for(int i = 0;i < strArr.length;i++) {
            arr[i] = Integer.parseInt(strArr[i]);
        }
        int max, min;

        if (arr.length == 1) {
            max = min = arr[0];
        }
        else {
            max = Arrays.stream(arr).max().orElse(0);
            min = Arrays.stream(arr).min().orElse(0);
        }
        return String.format("%d %d", max, min);
    }
}
