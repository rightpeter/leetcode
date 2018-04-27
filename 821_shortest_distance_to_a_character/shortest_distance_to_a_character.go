package shortest_distance_to_a_character

func shortestToChar(S string, C byte) []int {
	queue := [][]int{}
	ret := make([]int, len(S))

	for i, _ := range S {
		ret[i] = 10000
	}

	for i, cc := range S {
		if byte(cc) == C {
			ret[i] = 0
			if i-1 >= 0 {
				queue = append(queue, []int{i - 1, -1})
			}
			if i+1 < len(S) {
				queue = append(queue, []int{i + 1, 1})
			}
		}
	}

	for len(queue) > 0 {
		task := queue[0]
		queue = queue[1:]
		i := task[0]
		j := task[0] - task[1]

		if ret[j]+1 < ret[i] {
			ret[i] = ret[j] + 1
			if i+task[1] >= 0 && i+task[1] < len(S) {
				queue = append(queue, []int{i + task[1], task[1]})
			}
		}
	}

	return ret
}
