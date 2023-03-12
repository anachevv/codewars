/* Description
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
If you want to know more: http://en.wikipedia.org/wiki/DNA
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"

Link to the problem -> https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/java */

import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        System.out.println(checkResult("TTTT"));
        System.out.println(checkResult("TAACG"));
        System.out.println(checkResult("CATA"));
    }
    public static String checkResult(String dna) {
        String result = "";
        HashMap<Character, Character> letters = new HashMap<Character, Character>();
        letters.put('A', 'T'); letters.put('T', 'A');
        letters.put('C', 'G'); letters.put('G', 'C');

        for (int i = 0; i < dna.length(); i++) {
            result += letters.get(dna.charAt(i));
        }
        return result;
    }
}
