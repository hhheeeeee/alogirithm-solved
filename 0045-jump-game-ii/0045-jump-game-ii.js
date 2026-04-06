/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function (nums) {
    let memo = new Array(nums.length).fill("Infinity")
    
    if (nums.length < 2) return 0
    
    for (let start = 0; start <= nums[0]; start++) {
        memo[start] = 1
    }

    for (let i = 1; i < nums.length; i++) {
        let cur = nums[i]
        for (let j = 1; j < cur + 1; j++) {
            if (i + j < nums.length) {
                memo[i + j] = Math.min(memo[i] + 1, memo[i + j])
                if (i + j === nums.length - 1) {
                    return memo[nums.length - 1]
                }
            }
        }
    }
    return memo[nums.length - 1]
};