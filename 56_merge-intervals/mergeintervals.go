package mergeintervals

import (
	"sort"
)

// Interval Definition for an interval.
type Interval struct {
	Start int
	End   int
}

func merge(intervals []Interval) []Interval {
	if len(intervals) <= 0 {
		return intervals
	}

	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i].Start < intervals[j].Start
	})

	l := intervals[0].Start
	r := intervals[0].End
	mergedIntervals := []Interval{}

	for i := 1; i < len(intervals); i++ {
		if intervals[i].Start > r {
			mergedIntervals = append(mergedIntervals, Interval{Start: l, End: r})
			l = intervals[i].Start
			r = intervals[i].End
		} else {
			if intervals[i].End > r {
				r = intervals[i].End
			}
		}
	}

	mergedIntervals = append(mergedIntervals, Interval{Start: l, End: r})

	return mergedIntervals
}
