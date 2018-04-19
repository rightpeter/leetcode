package reverse_integer

const (
	MAX = 1<<31 - 1
	MIN = -MAX - 1
)

func reverse(x int) int {
	revIntArr := []int{}
	for tmp := x; tmp != 0; {
		revIntArr = append(revIntArr, tmp%10)
		tmp = tmp / 10
	}

	if len(revIntArr) == 0 {
		return x
	}

	i := 0
	for revIntArr[i] == 0 {
		i++
	}

	ret := 0
	for ; i < len(revIntArr); i++ {
		ret = ret*10 + revIntArr[i]
		if ret > 0 && ret > MAX || ret < 0 && ret < MIN {
			return 0
		}
	}

	return ret
}
