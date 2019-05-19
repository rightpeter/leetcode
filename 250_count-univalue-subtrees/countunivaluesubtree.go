// Package countunivaluesubtree provides ...
package countunivaluesubtree

// TreeNode ...
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isUnivalueSubTree(root *TreeNode) (bool, int) {
	if root == nil {
		return true, 0
	}

	if root.Left == nil && root.Right == nil {
		return true, 1
	}

	isLeft, leftCount := isUnivalueSubTree(root.Left)
	isRight, rightCount := isUnivalueSubTree(root.Right)

	if !isLeft || !isRight {
		return false, leftCount + rightCount
	}

	if root.Right == nil {
		if root.Val == root.Left.Val {
			return true, leftCount + 1
		}
		return false, leftCount
	}

	if root.Left == nil {
		if root.Val == root.Right.Val {
			return true, rightCount + 1
		}
		return false, rightCount
	}

	if root.Val == root.Left.Val && root.Val == root.Right.Val {
		return true, leftCount + rightCount + 1
	}

	return false, leftCount + rightCount
}

func countUnivalSubtrees(root *TreeNode) int {
	_, count := isUnivalueSubTree(root)

	return count
}
