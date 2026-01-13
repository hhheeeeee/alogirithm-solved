/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0])
    let [start, end] = intervals[0]
    let result = []
     for (let i = 1; i < intervals.length; i++) {
        const [nowStart, nowEnd] = intervals[i]; 
        if (nowStart <= end) {
             end = Math.max(nowEnd, end)
        } else {
            result.push([start, end]);
            [start, end] = [nowStart, nowEnd];
        }
    }
    result.push([start, end])
    return result
};