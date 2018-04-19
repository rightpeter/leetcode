package longest_substring

import (
	"testing"
)

func TestLenghthOfLongestSubstring(t *testing.T) {
	tests := []string{
		"abcabcbb",
		"bbbbb",
		"pwwkew",
	}

	results := []int{
		3,
		1,
		3,
	}

	caseNum := 3

	for i := 0; i < caseNum; i++ {
		if ret := lengthOfLongestSubstring(tests[i]); ret != results[i] {
			t.Fatalf("Case: %d, Fail: %v, Expect: %v\n", i, ret, results[i])
		}
	}
}
