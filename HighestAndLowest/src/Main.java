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
