package mergeintervals

import "testing"
import "reflect"

func TestTwoSum(t *testing.T) {
	tests := [][]Interval{
		[]Interval{
			Interval{1, 3},
			Interval{2, 6},
			Interval{8, 10},
			Interval{15, 18},
		},
		[]Interval{
			Interval{1, 4},
			Interval{4, 5},
		},
		[]Interval{
			Interval{1, 4},
			Interval{0, 4},
		},
		[]Interval{
			Interval{1, 4},
			Interval{2, 3},
		},
	}
	results := [][]Interval{
		[]Interval{
			Interval{1, 6},
			Interval{8, 10},
			Interval{15, 18},
		},
		[]Interval{
			Interval{1, 5},
		},
		[]Interval{
			Interval{0, 4},
		},
		[]Interval{
			Interval{1, 4},
		},
	}

	caseNum := 3
	for i := 0; i < caseNum; i++ {
		if ret := merge(tests[i]); !reflect.DeepEqual(ret, results[i]) {
			t.Fatalf("case %d fails: %v\n", i, ret)
		}
	}
}
