package add_two_numbers

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTool(l1 *ListNode, l2 *ListNode, extra int) (int, int) {
	tmpSum := l1.Val + l2.Val + extra
	sum := tmpSum % 10
	retExtra := tmpSum / 10

	return sum, retExtra
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	sumHead := ListNode{}
	l3 := &sumHead
	sum, extra := 0, 0

	sum, extra = addTool(l1, l2, extra)
	l3.Val = sum

	for l1.Next != nil && l2.Next != nil {
		l3.Next = &ListNode{}
		l1 = l1.Next
		l2 = l2.Next
		l3 = l3.Next

		sum, extra = addTool(l1, l2, extra)
		l3.Val = sum
	}

	tmpL := &ListNode{}
	if l1.Next != nil {
		tmpL = l1
	} else if l2.Next != nil {
		tmpL = l2
	}

	for tmpL.Next != nil {
		l3.Next = &ListNode{}
		tmpL = tmpL.Next
		l3 = l3.Next

		sum, extra = addTool(tmpL, &ListNode{0, nil}, extra)
		l3.Val = sum
	}

	if extra > 0 {
		l3.Next = &ListNode{}
		l3.Next.Val = extra
	}

	return &sumHead
}
