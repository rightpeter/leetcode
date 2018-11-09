package making_a_large_island

func findLand(i, j int, grid, tmpGrid [][]int) int {
	l := len(grid)
	queue := [][2]int{}

	if tmpGrid[i][j] == -1 {
		return -1
	}

	queue = append(queue, [2]int{i, j})

	for len(queue) > 0 {
		for di := -1; di <= 1; di++ {
			for dj := -1; dj <= 1; dj++ {
				if i+di >= 0 && i+di < l && j+dj >= 0 && j+dj < l {

				}
			}
		}
	}

}

func largestIsland(grid [][]int) int {
	l := len(grid)

	tmpGrid := [][]int{}
	for i := 0; i < l; i++ {
		for j := 0; j < l; j++ {
			tmpGrid[i][j] = 0
		}
	}

	for i := 0; i < l; i++ {
		for j := 0; j < l; j++ {
		}
	}
}
