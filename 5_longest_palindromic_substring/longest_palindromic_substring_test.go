package longest_palindromic_substring

import (
	"fmt"
	"testing"
)

func TestLongestPalindrome(t *testing.T) {
	tests := []string{
		"babad",
		"cbbd",
		"bbbbb",
		"a",
		"abcda",
		"babadada",
	}

	results := []string{
		"aba",
		"bb",
		"bbbbb",
		"a",
		"a",
		"adada",
	}

	caseNum := 6

	for i := 0; i < caseNum; i++ {
		fmt.Println("Case %d -----------------\n", i)
		if ret := longestPalindrome(tests[i]); ret != results[i] {
			t.Fatalf("Case %d, fails: %v, expect: %v\n", i, ret, results[i])
		}
	}
}
