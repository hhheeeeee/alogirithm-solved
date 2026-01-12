/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let subsum = new Array(nums.length).fill(0)

    subsum[0] = nums[0]

    for (let i = 1; i < nums.length; i++) {
        subsum[i] = Math.max(subsum[i-1] + nums[i], nums[i])
    }

    return Math.max(...subsum)
};