class Solution {
    calculateArea(s, e, heights) {
        let base = Math.max(s, e) - Math.min(s, e);
        let height = Math.min(heights[s], heights[e]);
        return base * height;
    }
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let [s, e, result] = [0, heights.length - 1, 0];

        while (s < e) {
            result = Math.max(result,this.calculateArea(s, e, heights))
            if (heights[s] < heights[e]) {
                s++;
            } else {
                e--;
            }
        }
        return result;
    }
}
