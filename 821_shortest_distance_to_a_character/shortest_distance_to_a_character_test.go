package shortest_distance_to_a_character

import (
	"fmt"
	"testing"
)

func testEq(a, b []int) bool {

	if a == nil && b == nil {
		return true
	}

	if a == nil || b == nil {
		return false
	}

	if len(a) != len(b) {
		return false
	}

	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}

func TestShortestToChar(t *testing.T) {
	tests := []string{
		"loveleetcode",
		"eeeeeeeeee",
	}

	bytes := []byte{
		'e',
		'e',
	}

	results := [][]int{
		[]int{3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0},
		[]int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
	}

	caseNum := 2
	for i := 0; i < caseNum; i++ {
		fmt.Printf("Case: %d, ----------------\n", i)

		if ret := shortestToChar(tests[i], bytes[i]); !testEq(ret, results[i]) {
			t.Fatalf("Case: %d, fails: %v, expects: %v\n", i, ret, results[i])
		}
	}
}
