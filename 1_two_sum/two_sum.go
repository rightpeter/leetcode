package two_sum

func twoSum(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		rest := target - nums[i]
		for j := i + 1; j < len(nums); j++ {
			if nums[j] == rest {
				return []int{i, j}
			}
		}
	}
	return nil
}
