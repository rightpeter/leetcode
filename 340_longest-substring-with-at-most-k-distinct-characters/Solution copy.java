import java.util.HashMap;
import java.util.Map;

class Solution {
  public static int lengthOfLongestSubstringKDistinct(String s, int k) {
    Map<Character, Integer> charMap = new HashMap<Character, Integer>();
    int charCount = 0;
    int ret = 0;

    System.out.println(s.length());

    if (k <= 0) {
      return ret;
    }

    int l = 0, r = 0;
    for (r = 0; r < s.length(); r++) {
      int tmpCount = charMap.getOrDefault(s.charAt(r), 0);
      if (tmpCount == 0) {
        charCount++;
      }
      charMap.put(s.charAt(r), tmpCount+1);

      if (charCount > k) {
        if (r-l > ret) {
          System.out.println(s.substring(l, r));
        }
        ret = Math.max(ret, r-l);
      }

      while (charCount > k && l < s.length()) {
        charMap.put(s.charAt(l), charMap.get(s.charAt(l))-1);
        if (charMap.get(s.charAt(l)) == 0) {
          charCount--;
        }
        l++;
      }
    }

    if (charCount <= k) {
      ret = Math.max(ret, r-l);
    }

    return ret;
  }

  public static void main(String[] args) {
    String s;
    int k, output, ret;
    s = "eceba";
    k = 2;
    output = 3;
    ret = lengthOfLongestSubstringKDistinct(s, k);
    System.out.println(
        String.format("Test 1 is %b, ret: (%s), output: (%s)", ret == output, ret, output));

    s = "aa";
    k = 1;
    output = 2;
    ret = lengthOfLongestSubstringKDistinct(s, k);
    System.out.println(
        String.format("Test 2 is %b, ret: (%s), output: (%s)", ret == output, ret, output));

    s = "abcabcabc";
    k = 2;
    output = 2;
    ret = lengthOfLongestSubstringKDistinct(s, k);
    System.out.println(
        String.format("Test 3 is %b, ret: (%s), output: (%s)", ret == output, ret, output));
  }
}
