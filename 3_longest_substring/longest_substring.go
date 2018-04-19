package longest_substring

func lengthOfLongestSubstring(s string) int {
	var letterRep = map[byte]int{}

	maxLen := 0
	for i, j := 0, -1; i < len(s); i++ {
		if last, ok := letterRep[s[i]]; ok {
			if last > j {
				j = last
			}
		}
		if i-j > maxLen {
			maxLen = i - j
		}
		letterRep[s[i]] = i
	}

	return maxLen
}
