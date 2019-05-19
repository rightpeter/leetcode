import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public static String mostCommonWord(String paragraph, String[] banned) {
        Set<String> bannedSet = new HashSet<String>();
        Map<String, Integer> wordsCount = new HashMap<String, Integer>();
        Integer maxCount = 0;
        String frequentWord = "";

        for (String word : banned) {
            bannedSet.add(word);
        }

        paragraph = paragraph.toLowerCase();
        paragraph = paragraph.replaceAll("([^a-z\\s])", " ");
        String[] words = paragraph.split("\\s+");
        for (String word : words) {
            if (bannedSet.contains(word)) {
                continue;
            }

            wordsCount.put(word, wordsCount.getOrDefault(word, 0) + 1 );
            if (wordsCount.get(word) > maxCount) {
                maxCount = wordsCount.get(word);
                frequentWord = word;
            }
        }

        return frequentWord;
    }

    public static void main(String[] args) {
        String paragraph, ret, output;
        String[] banned;
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.";
        banned = new String[]{"hit"};
        output = "ball";
        ret = mostCommonWord(paragraph, banned);
        System.out.println(String.format("Test 1 is %b, ret: (%s), output: (%s)", ret.equals(output), ret, output));

        paragraph = "a, a, a, a, b,b,b,c, c";
        banned = new String[]{"a"};
        output = "b";
        ret = mostCommonWord(paragraph, banned);
        System.out.println(String.format("Test 2 is %b, ret: (%s), output: (%s)", ret.equals(output), ret, output));
    }
}
