class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals, newInterval) {
        let result = [];
        let temp = [newInterval[0], newInterval[1]];
        let inserted = false;

        for (let i = 0; i < intervals.length; i++) {
            let [s, e] = intervals[i];

            if (e < temp[0]) {
                result.push([s, e]);
            } else if (s > temp[1]) {
                if (!inserted) {
                    result.push(temp);
                    inserted = true;
                }

                result.push([s, e]);
            } else {
                temp[0] = Math.min(temp[0], s);
                temp[1] = Math.max(temp[1], e);
            }
        }

        if (!inserted) {
            result.push(temp);
        }

        return result;
    }
}
