package valid_parentheses

var leftParentheses = map[byte]bool{
	'(': true,
	'[': true,
	'{': true,
}

var matchParentheses = map[byte]byte{
	')': '(',
	']': '[',
	'}': '{',
}

func isValid(s string) bool {
	stack := []byte{}
	for _, cc := range s {
		c := byte(cc)
		if leftParentheses[c] {
			stack = append(stack, c)
		} else {
			if len(stack) == 0 || stack[len(stack)-1] != matchParentheses[c] {
				return false
			} else {
				stack = stack[:len(stack)-1]
			}
		}
	}

	if len(stack) == 0 {
		return true
	} else {
		return false
	}
}
