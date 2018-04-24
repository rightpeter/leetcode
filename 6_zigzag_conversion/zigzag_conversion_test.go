package zigzag_conversion

import (
	"fmt"
	"testing"
)

func TestConvert(t *testing.T) {
	tests := []string{
		"PAYPALISHIRING",
		"PAYPALISHIRING",
		"A",
		"",
		"ASDFASDFSGUAIGASFD",
		"ABCDEFGHIJKLMNOPQ",
	}

	rowNums := []int{
		3,
		4,
		6,
		10,
		1,
		2,
	}

	results := []string{
		"PAHNAPLSIIGYIR",
		"PINALSIGYAHRPI",
		"A",
		"",
		"ASDFASDFSGUAIGASFD",
		"ACEGIKMOQBDFHJLNP",
	}

	caseNum := 6

	for i := 0; i < caseNum; i++ {
		fmt.Printf("Case %d -----------------\n", i)
		if ret := convert(tests[i], rowNums[i]); ret != results[i] {
			t.Fatalf("Case %d, fails: %v, expects: %v\n", i, ret, results[i])
		}
	}
}
