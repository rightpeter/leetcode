package card_flipping_game

func flipgame(fronts []int, backs []int) int {
	badNumbers := make(map[int]bool)
	for i := 0; i < len(fronts); i++ {
		if fronts[i] == backs[i] {
			badNumbers[fronts[i]] = true
		}
	}

	allNums := append(fronts, backs...)

	ret := 0

	for i := 0; i < len(allNums); i++ {
		if _, ok := badNumbers[allNums[i]]; !ok {
			if ret == 0 {
				ret = allNums[i]
			} else if allNums[i] < ret {
				ret = allNums[i]
			}
		}
	}

	return ret
}
