package zigzag_conversion

import (
	"bytes"
)

func convert(s string, numRows int) string {
	var buffer bytes.Buffer

	if numRows == 1 {
		return s
	}

	n := (numRows - 1) * 2
	m := len(s)/n + 1

	// if numRows == 1 {
	// 	return s
	// }

	for j := 0; j < m; j++ {
		if j*n < len(s) {
			buffer.WriteByte(s[j*n])
		}
	}

	for i := 2; i < numRows; i++ {
		for j := 0; j < m; j++ {
			if j*n+i-1 < len(s) {
				buffer.WriteByte(s[j*n+i-1])
			}
			if (j+1)*n-i+1 < len(s) {
				buffer.WriteByte(s[(j+1)*n-i+1])
			}
		}
	}

	for j := 0; j < m; j++ {
		if j*n+numRows-1 < len(s) {
			buffer.WriteByte(s[j*n+numRows-1])
		}
	}

	return buffer.String()
}
