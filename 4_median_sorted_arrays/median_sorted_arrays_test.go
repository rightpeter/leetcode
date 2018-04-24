package median_sorted_arrays

import (
	"testing"
)

func TestFindMedianSortedArrays(t *testing.T) {
	tests := [][][]int{
		[][]int{
			[]int{1, 3},
			[]int{2},
		},
		[][]int{
			[]int{1},
			[]int{1},
		},
		[][]int{
			[]int{3, 4},
			[]int{1, 2},
		},
		[][]int{
			[]int{5, 4},
			[]int{1, 2, 3},
		},
		[][]int{
			[]int{},
			[]int{1, 2, 3},
		},
		[][]int{
			[]int{1},
			[]int{2, 3, 4},
		},
	}

	results := []float64{
		2.0,
		1,
		2.5,
		3,
		2,
		2.5,
	}

	caseNum := 6

	for i := 0; i < caseNum; i++ {
		if ret := findMedianSortedArrays(tests[i][0], tests[i][1]); ret != results[i] {
			t.Fatalf("Case: %d, Fails: %v, Expects: %v\n", i, ret, results[i])
		}
	}
}
