package reverse_integer

import (
	"testing"
)

func TestReverse(t *testing.T) {
	tests := []int{
		123,
		-123,
		120,
		0,
		1534236469,
		900000,
	}

	results := []int{
		321,
		-321,
		21,
		0,
		0,
		9,
	}

	caseNum := 6
	for i := 0; i < caseNum; i++ {
		if ret := reverse(tests[i]); ret != results[i] {
			t.Fatalf("case %d fails: %v, expect: %v\n", i, ret, results[i])
		}
	}
}
