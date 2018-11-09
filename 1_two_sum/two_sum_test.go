package two_sum

import "testing"

func TestTwoSum(t *testing.T) {
	tests := [][]int{
		[]int{2, 7, 11, 15},
		[]int{3, 5, 6},
		[]int{6, 3, 4, 1},
	}
	targets := []int{
		9,
		11,
		4,
	}
	results := [][]int{
		[]int{0, 1},
		[]int{1, 2},
		[]int{1, 3},
	}
	caseNum := 3
	for i := 0; i < caseNum; i++ {
		if ret := twoSum(tests[i], targets[i]); ret[0] != results[i][0] || ret[1] != results[i][1] {
			t.Fatalf("case %d fails: %v\n", i, ret)
		}
	}
}
