package card_flipping_game

import (
	"fmt"
	"testing"
)

func TestFlipgame(t *testing.T) {
	tests := [][][]int{
		[][]int{
			[]int{1, 2, 4, 4, 7},
			[]int{1, 3, 4, 1, 3},
		},
		[][]int{
			[]int{1, 2, 4, 4, 7},
			[]int{1, 2, 4, 4, 7},
		},
		[][]int{
			[]int{1},
			[]int{2},
		},
	}

	results := []int{
		2,
		0,
		1,
	}

	caseNum := 3

	for i := 0; i < caseNum; i++ {
		fmt.Printf("Case: %d, -----------------\n", i)
		if ret := flipgame(tests[i][0], tests[i][1]); ret != results[i] {
			t.Fatalf("Case: %d, fails: %v, expect: %v\n", i, ret, results[i])
		}
	}
}
