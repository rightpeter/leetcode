package median_sorted_arrays

import (
	"math"
)

func findMedianIndex(numsL, numsS []int) (i, j int) {
	il := (len(numsL) - len(numsS)) / 2
	ir := (len(numsL) + len(numsS)) / 2
	if ir >= len(numsL) {
		ir = len(numsL) - 1
	}

	for il < ir {
		i = (il + ir) / 2
		j = (len(numsL)+len(numsS))/2 - i - 1

		if j < len(numsS)-1 && numsL[i] > numsS[j+1] {
			ir = i - 1
		} else if i < len(numsL)-1 && j > -1 && numsS[j] > numsL[i+1] {
			il = i + 1
		} else {
			return i, j
		}
	}

	return il, (len(numsL)+len(numsS))/2 - il - 1
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	numsL := []int{}
	numsS := []int{}

	if len(nums1) > len(nums2) {
		numsL = nums1
		numsS = nums2
	} else {
		numsL = nums2
		numsS = nums1
	}

	isOdd := (len(numsL)+len(numsS))%2 != 0

	i, j := findMedianIndex(numsL, numsS)

	if j == -1 {
		if isOdd {
			return float64(numsL[i])
		} else {
			return (float64(numsL[i]) + float64(numsL[i-1])) / 2
		}
	}

	if isOdd {
		return math.Max(float64(numsL[i]), float64(numsS[j]))
	} else {
		m1 := numsL[i]
		m2 := numsS[j]

		if j > 0 && numsS[j-1] > numsL[i] {
			m1 = numsS[j-1]
		}

		if i > 0 && numsL[i-1] > numsS[j] {
			m2 = numsL[i-1]
		}
		return (float64(m1) + float64(m2)) / 2
	}
}
