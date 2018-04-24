package longest_palindromic_substring

func longestPalindrome(s string) string {
	if len(s) <= 1 {
		return s
	}

	dp1 := make([]int, len(s))
	dp2 := make([]int, len(s))

	for i := 0; i < len(s); i++ {
		dp1[i] = 1
		dp2[i] = 1
	}

	key1 := true
	key2 := true

	l := 2
	il := 0
	lr := 1
	for (key1 || key2) && l <= len(s) {
		key1 = key2
		key2 = false
		dp := make([]int, len(s)-l+1)

		for i := 0; i <= len(s)-l; i++ {
			if s[i] == s[i+l-1] {
				dp[i] = dp1[i+1]
				if dp1[i+1] == 1 {
					il = i
					key2 = true
					lr = l
				}
			} else {
				dp[i] = 0
			}
		}
		dp1 = dp2
		dp2 = dp
		l++
	}

	return s[il : il+lr]
}
