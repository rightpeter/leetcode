package valid_parentheses

import (
	"testing"
)

func TestIsValid(t *testing.T) {
	tests := []string{
		"()",
		"()[]{}",
		"(]",
		"([)]",
		"{[]}",
		"]",
		"]](())]]",
		"(",
	}

	results := []bool{
		true,
		true,
		false,
		false,
		true,
		false,
		false,
		false,
	}

	caseNum := 8

	for i := 0; i < caseNum; i++ {
		if ret := isValid(tests[i]); ret != results[i] {
			t.Fatalf("Case %d fails: %v, expect: %v\n", i, ret, results[i])
		}
	}
}
