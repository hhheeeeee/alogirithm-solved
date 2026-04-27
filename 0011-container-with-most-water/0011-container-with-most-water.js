/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
    // [1,8,6,2,5,4,8,3,7]
    let result = 0
    let [s, e] = [0, height.length - 1]

    while (s < e) {
        result = Math.max((e - s) * Math.min(height[s], height[e]), result)
        if (height[s] < height[e]) {
            s++;
        } else {
            e--;
        }
    }

    return result
};
