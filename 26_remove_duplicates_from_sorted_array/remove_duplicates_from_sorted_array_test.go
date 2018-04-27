package remove_duplicates_from_sorted_array

import (
	"fmt"
	"testing"
)

func TestRemoveDuplicates(t *testing.T) {
	tests := [][]int{
		[]int{1, 1, 2},
		[]int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4},
		[]int{},
		[]int{0, 0, 0, 0},
	}

	results := []int{
		2,
		5,
		0,
		1,
	}

	caseNum := 4

	for i := 0; i < caseNum; i++ {
		fmt.Printf("Case %d: -------------------\n", i)

		if ret := removeDuplicates(tests[i]); ret != results[i] {
			t.Fatalf("Case %d, fails: %v, expects: %v\n", i, ret, results[i])
		}
	}
}
