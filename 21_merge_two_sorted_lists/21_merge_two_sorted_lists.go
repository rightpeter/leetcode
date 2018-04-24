package merge_two_sorted_lists

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	l3Head := ListNode{}
	l3 := &l3Head

	for l1 != nil && l2 != nil {

		if l2.Val < l1.Val {
			l3.Next = l2
			l2 = l2.Next
		} else {
			l3.Next = l1
			l1 = l1.Next
		}

		l3 = l3.Next
	}

	var lNotEmpty *ListNode
	if l1 != nil {
		lNotEmpty = l1
	} else if l2 != nil {
		lNotEmpty = l2
	}

	for lNotEmpty != nil {
		l3.Next = lNotEmpty
		lNotEmpty = lNotEmpty.Next
		l3 = l3.Next
	}
	return l3Head.Next
}
