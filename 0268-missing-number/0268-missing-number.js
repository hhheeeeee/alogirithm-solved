/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    // Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
    let totalSum = ((nums.length + 1) * nums.length) / 2
    let nowSum = nums.reduce((acc, cur) => acc + cur, 0)
    return totalSum - nowSum
};