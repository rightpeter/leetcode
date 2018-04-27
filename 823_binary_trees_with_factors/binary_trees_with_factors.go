package binary_trees_with_factors

import (
	"math"
	"sort"
)

func numFactoredBinaryTrees(A []int) int {
	sort.Ints(A)

	C := make(map[int]int)

	for i := 0; i < len(A); i++ {
		C[A[i]] = 1
		for j := 0; j < i; j++ {
			if _, ok := C[A[i]/A[j]]; A[i]%A[j] == 0 && ok {
				C[A[i]] += C[A[j]] * C[A[i]/A[j]]
			}
		}
	}

	ret := 0
	for i := 0; i < len(A); i++ {
		ret += C[A[i]]
		ret = ret % (int(math.Pow10(9)) + 7)
	}

	return ret
}
