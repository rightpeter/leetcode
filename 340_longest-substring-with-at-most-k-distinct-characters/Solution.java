import java.util.HashMap;
import java.util.Map;

public class Solution {
  // METHOD SIGNATURE BEGINS, THIS METHOD IS REQUIRED
  static int countKDistinctSubstrings(String inputString, int num) {
    // WRITE YOUR CODE HERE
    int ret = 0;
    int l = 0, r = 0;
    Map<Character, Integer> wordMap = new HashMap<Character, Integer>();
    int charCount = 0;

    if (num <= 0) {
      return ret;
    }

    for (r = 0; r < inputString.length(); r++) {
      char charL = inputString.charAt(l);
      char charR = inputString.charAt(r);

      int tmpCount = wordMap.getOrDefault(charR, 0);
      if (tmpCount == 0) {
        charCount++;
      }
      wordMap.put(charR, tmpCount + 1);

      if (charCount > num) {

        while (charCount > num && l < inputString.length()) {
          ret++;
          jp.put(charL, wordMap.get(charL) - 1);
          if (wordMap.get(charL) == 0) {
            charCount--;
          }
          l++;
        }
      }
    }

    if (charCount == num) {
      ret++;
    }

    return ret;
  }

  public static void main(String[] args) {
    String s;
    int k, output, ret;
    s = "abc";
    k = 2;
    output = 2;
    ret = countKDistinctSubstrings(s, k);
    System.out.println(
        String.format("Test 1 is %b, ret: (%s), output: (%s)", ret == output, ret, output));

    s = "abafg";
    k = 1;
    output = 5;
    ret = countKDistinctSubstrings(s, k);
    System.out.println(
        String.format("Test 2 is %b, ret: (%s), output: (%s)", ret == output, ret, output));

    s = "";
    k = 0;
    output = 2;
    ret = countKDistinctSubstrings(s, k);
    System.out.println(
        String.format("Test 3 is %b, ret: (%s), output: (%s)", ret == output, ret, output));
  }
}
