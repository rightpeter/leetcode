package remove_duplicates_from_sorted_array

func removeDuplicates(nums []int) int {
	i := 0
	for i < len(nums) {
		j := i

		for j+1 < len(nums) && nums[j+1] == nums[j] {
			j++
		}

		if j == len(nums)-1 {
			nums = nums[0 : i+1]
		} else {
			nums = append(nums[0:i+1], nums[j+1:]...)
		}

		i++
	}

	return len(nums)
}
