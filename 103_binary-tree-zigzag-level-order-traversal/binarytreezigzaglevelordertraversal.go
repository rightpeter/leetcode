package binarytreezigzaglevelordertraversal

// TreeNode ...
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// QueueElement ...
type QueueElement struct {
	node  *TreeNode
	level int
}

func reverse(order []int) {
	for i := 0; i < len(order)/2; i++ {
		j := len(order) - i - 1
		order[i], order[j] = order[j], order[i]
	}
}

func zigzagLevelOrder(root *TreeNode) [][]int {
	queue := []QueueElement{}
	order := [][]int{}

	if root == nil {
		return order
	}
	queue = append(queue, QueueElement{root, 0})

	for len(queue) > 0 {
		var head QueueElement
		head, queue = queue[0], queue[1:]
		if len(order)-1 < head.level {
			order = append(order, []int{})
		}
		order[head.level] = append(order[head.level], head.node.Val)

		if head.node.Left != nil {
			queue = append(queue, QueueElement{head.node.Left, head.level + 1})
		}

		if head.node.Right != nil {
			queue = append(queue, QueueElement{head.node.Right, head.level + 1})
		}
	}

	for i, list := range order {
		if i%2 == 1 {
			reverse(list)
		}
	}

	return order
}
