class Solution {
    private static String findLongestPalindromic(int l, int r, String s) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r))
        {
            l--;
            r++;
        }
        return s.substring(l+1, r);
    }
    public static String longestPalindrome(String s) {
        String ret = "", tmp;

        for (int i = 0; i < s.length(); i++) {
            tmp = findLongestPalindromic(i, i, s);
            if (tmp.length() > ret.length()) {
                ret = tmp;
            }

            tmp = findLongestPalindromic(i, i+1, s);
            if (tmp.length() > ret.length()) {
                ret = tmp;
            }
        }

        return ret;
    }
    public static void main(String[] args) {
        String input, output, ret;
        input = "babad";
        output = "bab";
        ret = longestPalindrome(input);
        System.out.println(String.format("Test 1 is %b, ret: (%s), output: (%s)", ret.equals(output), ret, output));

        input = "cbbd";
        output = "bb";
        ret = longestPalindrome(input);
        System.out.println(String.format("Test 2 is %b, ret: (%s), output: (%s)", ret.equals(output), ret, output));
    }
}