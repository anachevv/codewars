public class Solution {
    public static void main(String[] args) {
        System.out.println(isAscOrder(new int[] {1, 2, 3}));
        System.out.println(isAscOrder(new int[] {1, 4, 13, 97, 508, 1047, 20058}));
        System.out.println(isAscOrder(new int[] {56, 98, 123, 67, 742, 1024, 32, 90969}));
    }
    public static boolean isAscOrder(int[] arr) {
        int last = arr[0];
        boolean isSorted = true;

        for (int idx=1;idx < arr.length;++idx) {
            if (arr[idx] < last) {
                isSorted = false;
                break;
            }
            last = arr[idx];
        }
        return isSorted;
    }
}
