package uniquebinarysearchtrees

import (
	"fmt"
	"testing"
)

func TestUniqueBinarySearchTrees(t *testing.T) {
	tests := []int{3, 0, 1, 2, 4}
	results := []int{5, 1, 1, 2, 14}

	caseNum := 1

	for i := 0; i < caseNum; i++ {
		fmt.Printf("Case %d: ---------------", i)

		if ret := numTrees(tests[i]); ret != results[i] {
			t.Fatalf("Case: %d, fails: %d, expect: %d\n", i, ret, results[i])
		}
	}
}
