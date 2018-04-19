package add_two_numbers

import (
	"fmt"
	"testing"
)

func intToNodeList(x int) *ListNode {
	listHead := ListNode{}
	tmpL := &listHead
	tmpL.Val = x % 10
	x = x / 10

	for x > 0 {
		tmpL.Next = &ListNode{}
		tmpL = tmpL.Next
		tmpL.Val = x % 10
		x = x / 10
	}

	return &listHead
}

func nodeListToInt(l *ListNode) int {
	if l.Next == nil {
		return l.Val
	} else {
		return nodeListToInt(l.Next)*10 + l.Val
	}
}

func printListNode(l *ListNode) {
	fmt.Print(l.Val)
	for l.Next != nil {
		l = l.Next
		fmt.Printf(" -> %d", l.Val)
	}
	fmt.Println("")
}

func TestAddTwoNumbers(t *testing.T) {

	tests := [][]int{
		{342, 465},
		{0, 123214},
		{235132, 23441234},
		{0, 0},
	}

	caseNum := 4
	for i := 0; i < caseNum; i++ {
		l1, l2 := intToNodeList(tests[i][0]), intToNodeList(tests[i][1])
		l3 := addTwoNumbers(l1, l2)

		fmt.Printf("Case %d --------------------------------\n", i)
		printListNode(l1)
		printListNode(l2)
		printListNode(l3)

		if tests[i][0]+tests[i][1] != nodeListToInt(l3) {
			t.Fatalf("case %d fails: %v, expect: %v\n", i, nodeListToInt(l3), tests[i][0]+tests[i][1])
		}
		fmt.Println("")
	}
}
