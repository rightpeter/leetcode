package merge_two_sorted_lists

import (
	"fmt"
	"testing"
)

func intSliceToNodeList(x []int) *ListNode {
	if len(x) == 0 {
		return nil
	}
	listHead := ListNode{Val: x[0]}
	tmpL := &listHead

	for i := 1; i < len(x); i++ {
		tmpL.Next = &ListNode{Val: x[i]}
		tmpL = tmpL.Next
	}

	return &listHead
}

func printListNode(l *ListNode) {
	if l == nil {
		fmt.Println("")
		return
	}
	fmt.Print(l.Val)
	for l.Next != nil {
		l = l.Next
		fmt.Printf(" -> %d", l.Val)
	}
	fmt.Println("")
}

func compareTwoListNode(l1, l2 *ListNode) bool {
	for l1 != nil && l2 != nil {
		if l1.Val != l2.Val {
			return false
		}

		l1 = l1.Next
		l2 = l2.Next
	}

	if l1 != nil || l2 != nil {
		return false
	}

	return true
}

func TestMergeTwoLists(t *testing.T) {
	tests := [][][]int{
		[][]int{
			[]int{1, 2, 4},
			[]int{1, 3, 4},
		},
		[][]int{
			[]int{},
			[]int{},
		},
		[][]int{
			[]int{},
			[]int{1, 3, 4},
		},
		[][]int{
			[]int{1, 2, 4},
			[]int{},
		},
	}

	results := [][]int{
		[]int{1, 1, 2, 3, 4, 4},
		[]int{},
		[]int{1, 3, 4},
		[]int{1, 2, 4},
	}

	caseNum := 4

	for i := 0; i < caseNum; i++ {
		l1, l2 := intSliceToNodeList(tests[i][0]), intSliceToNodeList(tests[i][1])
		l3 := mergeTwoLists(l1, l2)

		fmt.Printf("Case %d ---------------------\n", i)
		fmt.Print("L1: ")
		printListNode(l1)
		fmt.Print("L2: ")
		printListNode(l2)
		fmt.Print("L3: ")
		printListNode(l3)

		if !compareTwoListNode(l3, intSliceToNodeList(results[i])) {
			t.Fatalf("case %d, fails: %v, expect: %v\n", i, i, results[i])
		}
	}
}
