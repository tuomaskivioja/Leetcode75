
# Insert Interval
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    left, right = [], []
    start, end = newInterval[0], newInterval[1]

    for interval in intervals:
        if interval[1] < start:
            left.append(interval)
        elif interval[0] > end:
            right.append(interval)
        else:
            start = min(start, interval[0])
            end = max(end, interval[1])

    return left + [[start, end]] + right

# Merge Intervals
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# Non-overlapping Intervals
def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    count = 1
    for interval in intervals[1:]:
        if interval[0] >= end:
            end = interval[1]
            count += 1
    return len(intervals) - count

# Meeting Rooms (Leetcode Premium)
def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

# Meeting Rooms II (Leetcode Premium)
def minMeetingRooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    s, e = 0, 0
    numRooms, available = 0, 0
    while s < len(starts):
        if starts[s] < ends[e]:
            if available == 0:
                numRooms += 1
            else:
                available -= 1
            s += 1
        else:
            available += 1
            e += 1
    return numRooms
